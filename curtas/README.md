# MDP Curtas

Modelos das artes do **MDP Curtas**, o meetup presencial da Mulheres de Produto, e do **mídia kit Curtas para Empresas**. Aprovados pela diretoria em novembro de 2026.

![Feed com 1 palestrante](previews/feed-1-palestrante.png)

## O que tem aqui

```
curtas/
  AGENTS.md            Regras e processo para agentes de IA (leia primeiro)
  especificacao.md     Cores, fontes, medidas e composições de cada peça
  modelos/             Modelos em HTML com campos {{...}} (fonte da verdade do layout)
    modelos.json       Lista de modelos, tamanhos e campos
  assets/
    formas/            Blobs e contornos oficiais (SVG)
    fontes/            Montserrat (OFL)
    fotos-exemplo/     Fotos usadas nos exemplos
    composicoes.json   Posição das fotos e dos blobs para 1, 2 e 3 palestrantes
  ferramentas/
    gerar.py           Preenche os modelos e gera os PNGs (e o PDF do mídia kit)
  exemplos/            Arquivos de dados prontos para copiar
  previews/            Como cada peça fica
```

## Peças

| Peça | Tamanho | Versões |
|---|---|---|
| Feed (Instagram e LinkedIn) | 1080 x 1350 | 1, 2 e 3 palestrantes |
| Story | 1080 x 1920 | 1, 2 e 3 palestrantes |
| Capa do evento (Luma) | 1080 x 1080 | 1, 2 e 3 palestrantes |
| Slide de abertura | 1920 x 1080 | única |
| Slide da palestrante | 1920 x 1080 | uma por palestrante |
| Mídia kit Curtas para Empresas | 1920 x 1080 | 10 slides |

## Como gerar as artes de um evento novo

1. Copie um arquivo de `exemplos/` (por exemplo `curtas-sp-2-palestrantes.json`).
2. Troque os textos, a data, o horário, o local, os nomes e os caminhos das fotos.
3. Rode:
   ```
   pip install playwright pillow
   python3 -m playwright install chromium
   python3 curtas/ferramentas/gerar.py curtas/exemplos/seu-evento.json
   ```
4. Os PNGs aparecem na pasta `saida` indicada no arquivo.

Com o Claude ou outro agente, basta pedir: "gere as artes do Curtas com estes dados" e enviar as fotos. O agente segue o `AGENTS.md`.

## Regras principais

- Identidade da marca Mulheres de Produto, nunca a do Festival.
- Fundo branco. Fotos sempre dentro dos blobs oficiais.
- 1 palestrante: só a foto dela. 2 ou 3 palestrantes: fotos delas e a host do dia menor.
- Frases sem ponto final. Título em até 3 linhas.

A lista completa está em `AGENTS.md`.
