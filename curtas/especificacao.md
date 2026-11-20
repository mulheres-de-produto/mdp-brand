# MDP Curtas: especificação das peças

Medidas em pixels CSS no tamanho final de cada peça. Os HTML em `modelos/` implementam exatamente esta especificação. Se houver diferença entre este documento e um modelo, vale o modelo.

## Cores

Valores da paleta "MDP 2026" do kit de marca no Canva. Use estes para tudo que não é o arquivo do logo.

| Nome | HEX | Uso |
|---|---|---|
| Branco | `#FFFFFF` | Fundo de todas as peças de divulgação e slides do evento |
| Preto texto | `#141414` | Títulos, textos, ícones, contornos |
| Cinza texto | `#4A4A4A` | Bio e textos de apoio |
| Rosa | `#F964A5` | Etiquetas, nome em destaque, botão, blobs chapados |
| Rosa claro | `#F2D1E0` | Blobs chapados de fundo, divisores |
| Laranja | `#F78052` | Blobs chapados |
| Amarelo | `#E9CE33` | Blobs chapados, fundo de um slide do mídia kit |
| Fundo da etiqueta | `#FDEEF5` | Preenchimento das etiquetas em pílula |

O arquivo do logo (`marca/svg/`) usa os valores originais da marca (`#F4609C` e `#E8CE31`). Não altere o logo.

## Tipografia

Montserrat em todas as peças. Os arquivos estão em `assets/fontes/` (licença OFL).

| Elemento | Peso | Outros |
|---|---|---|
| Título | 700 (Bold) | entrelinha 1.14, espaçamento -0.005em, centralizado nos posts |
| Etiqueta (pílula) | 700 | caixa alta, espaçamento 0.06em, cor rosa |
| Etiqueta de nome na foto | 600 | fundo branco, borda rosa, preto texto |
| "Host" na etiqueta | 700 | rosa, seguido de " · Nome" |
| Informações (data, horário, local) | 500 | ícones de traço, 1.15 vezes o tamanho da fonte |
| Botão do story | 700 | caixa alta, espaçamento 0.06em, branco sobre rosa |

## Componentes

**Etiqueta em pílula** (ex.: "CURTAS · SÃO PAULO", "PALESTRANTE DA NOITE")
- Fundo `#FDEEF5`, borda rosa de `max(2, tamanho/9)` px, texto rosa.
- Espaçamento interno: 0.55 vez o tamanho da fonte na vertical, 1.3 vez na horizontal. Cantos totalmente arredondados.

**Etiqueta de nome sobre a foto**
- Fundo branco, borda rosa, cantos totalmente arredondados, centralizada no ponto indicado na composição.
- Fica na borda de baixo da foto, sem cobrir o rosto.

**Linha de informações**
- Linha 1: ícone de calendário + data, ícone de relógio + horário.
- Linha 2: ícone de local + local.
- Ícones: traço de 1.9 em 24 px, cor `#141414`, cantos arredondados.

**Botão do story**
- "INSCRIÇÕES NO LINK DA BIO", rosa com texto branco, 28 px, espaçamento interno 24 x 52 px.
- No mínimo 72 px de respiro acima e 64 px abaixo até o logo.

## Formas

Todas extraídas do arquivo de referência da diretoria (`marca/pdf/mdp-composicao-fotos-formas.pdf`).

| Arquivo | Uso |
|---|---|
| `forma-0.svg` | Foto da palestrante 1 |
| `forma-7.svg` | Foto da palestrante 2 |
| `forma-2.svg` | Foto da palestrante 3 |
| `forma-1.svg` | Foto da host |
| `forma-4.svg` | Blob chapado rosa claro |
| `forma-3.svg` | Blob chapado rosa |
| `forma-6.svg` e `forma-5.svg` | Blobs chapados laranja |
| `contorno-espiral.svg` | Contorno preto em espiral |
| `contorno-concentrico.svg` | Contorno preto concêntrico |

As formas de foto funcionam como máscara: a foto preenche a forma inteira (`object-fit: cover`) e a forma é esticada para a caixa da foto.

## Composições de fotos

`assets/composicoes.json` guarda a posição de cada elemento numa caixa de referência de 1000 x 820. Cada peça escala essa caixa para a largura dela (feed 860, story 960, capa 740, slide da palestrante 960). A ordem dos elementos é a ordem das camadas, de trás para frente.

- **1 palestrante:** foto grande (forma-0, largura 580) no centro. Blobs chapados atrás, contornos à frente. Sem host.
- **2 palestrantes:** duas fotos do mesmo tamanho (largura 440), lado a lado em leve degrau. Host (largura 190) no alto à direita.
- **3 palestrantes:** três fotos parecidas (larguras 360, 360 e 350) em leve degrau. Host (largura 170) no alto à direita.

## Peças

### Feed 4:5 (1080 x 1350)
- Margens: 64 topo, 70 laterais, 60 base.
- Composição: largura 860.
- Etiqueta da cidade: 24 px, 34 px abaixo da composição.
- Título: 52 px, 26 px abaixo da etiqueta.
- Informações: 26 px, 28 px abaixo do título.
- Logo: altura 64 px, encostado na margem de baixo.

### Story 9:16 (1080 x 1920)
- Margens: 210 topo, 60 laterais, 170 base (área segura do Instagram).
- Composição: largura 960.
- Etiqueta: 28 px, 50 px abaixo. Título: 64 px, 34 px abaixo. Informações: 30 px, 38 px abaixo.
- Botão e logo (72 px) no rodapé, 64 px entre eles.

### Capa do evento 1:1 (1080 x 1080)
- Margens: 56 topo, 70 laterais, 54 base.
- Composição: largura 740.
- Etiqueta: 22 px, 28 px abaixo. Título: 44 px, 20 px abaixo.
- Sem data e sem local. Logo: altura 54 px.

### Slide de abertura (1920 x 1080)
- À esquerda, só grafismo (sem foto), numa área de 800 x 900.
- À direita: etiqueta da cidade 28 px, "Nosso papo já vai começar" 92 px em duas linhas, "Sejam bem-vindas" 38 px rosa, logo 76 px.

### Slide da palestrante (1920 x 1080)
- À esquerda, composição de 1 palestrante com largura 960, sem etiqueta de nome.
- À direita: "PALESTRANTE DA NOITE" 26 px, nome 104 px em duas linhas, cargo 38 px rosa, bio 28 px cinza (máximo 3 linhas, largura 720).
- Rodapé: logo 60 px, divisor rosa claro e "Curtas Cidade" 24 px.

### Mídia kit Curtas para Empresas (10 slides de 1920 x 1080)
1. Capa
2. O que é o Curtas para Empresas
3. Por que levar o Curtas (3 colunas numeradas)
4. Como funciona (fundo rosa, logo branco)
5. Descrição da experiência
6. A dinâmica das 3 horas (fundo rosa claro, linha do tempo com blobs numerados)
7. O que está incluso (5 itens numerados)
8. Investimento (valor em destaque e card de contrapartida)
9. Depoimentos (fundo amarelo, 5 depoimentos)
10. Vamos juntas? (contato)

Os textos do mídia kit estão nos próprios modelos. Os campos variáveis são o valor, o valor por extenso, o contato e as fotos de evento (`foto_evento_1` a `foto_evento_6`).
