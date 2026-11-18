# MDP Curtas: instruções para agentes de IA

Este arquivo vale para qualquer agente (Claude, Codex, Gemini e outros) que for criar artes do **MDP Curtas** ou do **mídia kit Curtas para Empresas**. Leia inteiro antes de gerar qualquer peça.

As artes foram aprovadas pela diretoria da Associação Mulheres de Produto em novembro de 2026. O trabalho do agente é **preencher os modelos com as informações reais de cada evento**, sem mudar o layout. Qualquer mudança de layout, cor, fonte, tamanho ou posição precisa de aprovação da diretoria antes.

## Ordem de leitura

1. Este arquivo (regras e processo).
2. `especificacao.md` (medidas, cores, fontes e composições de cada peça).
3. `modelos/modelos.json` (lista de modelos e campos de cada um).
4. Um exemplo em `exemplos/` parecido com o evento que você vai divulgar.

## Como gerar as artes (caminho padrão)

1. Copie o exemplo mais parecido de `exemplos/` (1, 2 ou 3 palestrantes, ou o mídia kit).
2. Troque só os valores dos campos: textos, data, horário, local, nomes e caminhos das fotos.
3. Rode:
   ```
   pip install playwright pillow
   python3 -m playwright install chromium
   python3 curtas/ferramentas/gerar.py caminho/do/seu-evento.json
   ```
4. Os PNGs saem na pasta indicada em `saida`, no tamanho certo de cada peça.
5. Abra cada PNG e confira as regras abaixo antes de entregar.

Os HTML em `modelos/` são a fonte da verdade do layout. **Não edite os modelos para encaixar um conteúdo.** Se o conteúdo não cabe, ajuste o conteúdo (veja "Quando o texto não cabe").

## Regras inegociáveis

**Marca**
- O Curtas usa a identidade da marca Mulheres de Produto. Nunca a identidade do Festival.
- Logo: só os arquivos de `marca/svg/`. O símbolo M fica sempre à esquerda do texto. Não invente variações.

**Fundo e cor**
- Nos posts, no story, na capa e nos slides do evento, o fundo é sempre branco. O rosa nunca é fundo dessas peças, porque pesa demais.
- Só no mídia kit existem slides com fundo rosa, rosa claro ou amarelo, para quebrar a sequência. Esses slides já estão definidos nos modelos.
- Use só as cores de `especificacao.md`.

**Formas (blobs)**
- Os blobs da marca são triângulos bem arredondados. Use só as formas de `assets/formas/`.
- Nunca transforme um blob em folha, balão de fala, círculo ou qualquer outra forma.
- Blobs decorativos são grandes e parecem grafismo. Nunca use blobs pequenos que pareçam pontinhos, ícones ou marcadores de informação.
- Contornos (espiral e concêntrico) são sempre pretos.
- O grafismo é apoio: nunca chama mais atenção que a foto e o título.

**Fotos**
- Foto de pessoa vai sempre dentro de um blob, sem cortar o blob. Nunca em círculo ou retângulo.
- Posts de palestrante mostram **só as fotos das palestrantes**. Nunca fotos aleatórias de evento.
- **1 palestrante:** só a foto dela. Nenhuma outra foto na peça, nem a da host.
- **2 ou 3 palestrantes:** as fotos das palestrantes em tamanhos parecidos e a foto da host do dia menor, no alto à direita, com a etiqueta "Host · Nome". A host aparece para dar visibilidade às embaixadoras.
- Use fotos com o rosto centralizado, em boa resolução (mínimo 800 x 800 px), recortadas em quadrado.

**Texto**
- Frases de arte não levam ponto final.
- Sem sombra, contorno ou efeito de deslocamento na tipografia.
- Título com no máximo 3 linhas, com quebra manual (`\n` no JSON), cerca de 28 caracteres por linha.
- Data por extenso e minúscula ("29 de setembro"), horário curto ("19h").
- A capa do evento (Luma) não leva data nem local, porque a plataforma já mostra.
- Na etiqueta da cidade, a cidade vai em caixa alta ("CURTAS · SÃO PAULO"). O gerador faz isso sozinho a partir do campo `cidade`.

**Respiro**
- Botões e chamadas ("INSCRIÇÕES NO LINK DA BIO") nunca encostam em texto. Os modelos já reservam o espaço.
- Etiquetas de nome não cobrem o rosto da pessoa.

## Quando o texto não cabe

- Título com mais de 3 linhas: proponha uma versão mais curta e peça aprovação a quem pediu a arte. Não diminua a fonte.
- Nome muito longo na etiqueta da foto: use nome e sobrenome principal ("Ana Souza", não "Ana Maria de Souza Oliveira").
- Local muito longo: use o nome do lugar e, se precisar, o bairro ("Stone · Av. Rebouças 2880").
- Mais de 3 palestrantes: não existe modelo. Fale com a diretoria antes de criar um.

## Quando usar cada modelo

| Situação | Modelos |
|---|---|
| Divulgação no feed (Instagram e LinkedIn) | `feed-1-palestrante`, `feed-2-palestrantes`, `feed-3-palestrantes` |
| Story de divulgação | `story-1-palestrante`, `story-2-palestrantes`, `story-3-palestrantes` |
| Capa da página do evento (Luma) | `capa-evento-1-palestrante`, `capa-evento-2-palestrantes`, `capa-evento-3-palestrantes` |
| Telão, antes de começar | `slide-abertura` |
| Telão, apresentação de cada palestrante | `slide-palestrante` (um por palestrante) |
| Proposta para empresas | `midia-kit-01` a `midia-kit-10` |

## Como trabalhar com a equipe

- Mostre a prévia antes de publicar ou enviar.
- Antes de mudar um texto, explique o motivo da mudança.
- Português, frases curtas, listas, sem emojis e sem travessões.
- Não publique fotos de pessoas sem a autorização delas.
