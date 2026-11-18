#!/usr/bin/env python3
"""Gera as artes do MDP Curtas a partir dos modelos aprovados.

Uso:
    python3 curtas/ferramentas/gerar.py curtas/exemplos/curtas-sp-1-palestrante.json

O arquivo de dados diz quais modelos gerar e quais textos e fotos entram em
cada campo. O layout vem dos HTML em curtas/modelos/ e nunca é alterado por
este script: ele só preenche os campos {{...}} e tira a foto da página.

Requisitos:
    pip install playwright pillow
    python3 -m playwright install chromium
"""
import argparse
import asyncio
import html
import json
import os
import re
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]          # curtas/
MODELOS = RAIZ / "modelos"
FOTOS_EXEMPLO = RAIZ / "assets" / "fotos-exemplo"

# Fotos padrão do mídia kit (fotos da comunidade usadas no material da marca).
PADRAO = {
    "foto_evento_1": FOTOS_EXEMPLO / "evento-palco-2.jpg",
    "foto_evento_2": FOTOS_EXEMPLO / "evento-conversa-1.jpg",
    "foto_evento_3": FOTOS_EXEMPLO / "evento-conversa-2.jpg",
    "foto_evento_4": FOTOS_EXEMPLO / "evento-abraco-2.jpg",
    "foto_evento_5": FOTOS_EXEMPLO / "evento-palco-1.jpg",
    "foto_evento_6": FOTOS_EXEMPLO / "foto-exemplo-4.jpg",
    "valor": "R$ 7.000",
    "valor_por_extenso": "sete mil reais",
    "contato_nome": "Erika Oliveira",
    "contato_cargo": "Líder de Iniciativa",
    "contato_email": "erika.oliveira@mulheresdeproduto.com",
}

CAMPOS_COM_QUEBRA = {"titulo", "bio", "nome_palestrante"}


def carregar_manifesto():
    return {m["modelo"]: m for m in json.loads((MODELOS / "modelos.json").read_text())}


def resolver_foto(valor, base):
    caminho = Path(valor)
    if not caminho.is_absolute():
        caminho = (base / caminho).resolve()
    if not caminho.exists():
        sys.exit(f"Foto não encontrada: {caminho}")
    return caminho.as_uri()


def preencher(modelo_html, campos, base):
    def troca(m):
        chave = m.group(1)
        if chave not in campos:
            sys.exit(f"Falta o campo '{chave}' no arquivo de dados")
        valor = campos[chave]
        if chave.startswith("foto_"):
            return resolver_foto(valor, base)
        texto = html.escape(str(valor))
        if chave in CAMPOS_COM_QUEBRA:
            texto = texto.replace("\n", "<br>")
        return texto
    return re.sub(r"\{\{(\w+)\}\}", troca, modelo_html)


async def gerar(dados_path, escala):
    from playwright.async_api import async_playwright

    dados_path = Path(dados_path).resolve()
    base = dados_path.parent
    dados = json.loads(dados_path.read_text())
    manifesto = carregar_manifesto()
    saida = (base / dados.get("saida", "saida")).resolve()
    saida.mkdir(parents=True, exist_ok=True)

    comuns = dict(PADRAO)
    comuns.update(dados.get("campos", {}))
    if "cidade" in comuns and "cidade_maiusculas" not in comuns:
        comuns["cidade_maiusculas"] = comuns["cidade"].upper()

    gerados = []
    async with async_playwright() as p:
        opcoes = {"args": ["--allow-file-access-from-files"]}
        if os.environ.get("CHROME_PATH"):          # opcional: usar um Chrome já instalado
            opcoes["executable_path"] = os.environ["CHROME_PATH"]
        navegador = await p.chromium.launch(**opcoes)
        for peca in dados["pecas"]:
            nome = peca["modelo"]
            if nome not in manifesto:
                sys.exit(f"Modelo desconhecido: {nome}. Veja curtas/modelos/modelos.json")
            m = manifesto[nome]
            campos = dict(comuns)
            campos.update(peca.get("campos", {}))
            if "cidade" in campos and "cidade_maiusculas" not in peca.get("campos", {}):
                campos["cidade_maiusculas"] = campos["cidade"].upper()
            for k, v in list(campos.items()):
                if isinstance(v, Path):
                    campos[k] = str(v)
            conteudo = preencher((MODELOS / f"{nome}.html").read_text(), campos, base)
            # O HTML preenchido fica na pasta dos modelos para os caminhos relativos funcionarem.
            with tempfile.NamedTemporaryFile("w", suffix=".html", dir=MODELOS, delete=False) as tmp:
                tmp.write(conteudo)
                tmp_path = Path(tmp.name)
            try:
                pagina = await navegador.new_page(
                    viewport={"width": m["largura"], "height": m["altura"]},
                    device_scale_factor=escala,
                )
                await pagina.goto(tmp_path.as_uri())
                await pagina.evaluate("document.fonts.ready")
                await pagina.wait_for_timeout(300)
                arquivo = saida / f"{peca.get('arquivo', nome)}.png"
                await pagina.screenshot(path=str(arquivo))
                await pagina.close()
                gerados.append(arquivo)
                print(f"ok  {arquivo}")
            finally:
                tmp_path.unlink(missing_ok=True)
        await navegador.close()

    if dados.get("pdf"):
        from PIL import Image
        paginas = [Image.open(f).convert("RGB") for f in gerados]
        pdf = saida / f"{dados['pdf']}.pdf"
        paginas[0].save(pdf, save_all=True, append_images=paginas[1:], resolution=72 * escala)
        print(f"ok  {pdf}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dados", help="arquivo JSON com os campos e as peças")
    ap.add_argument("--escala", type=float, default=1, help="1 = tamanho do Instagram (padrão), 2 = alta resolução")
    args = ap.parse_args()
    asyncio.run(gerar(args.dados, args.escala))


if __name__ == "__main__":
    main()
