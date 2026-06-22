# RELATÓRIO DE EXPLORAÇÃO DA FONTE — DIOE AVARÉ

## Integrantes

Grupo:

* Jorge Augusto — RA 848435
* Adrian Soares — RA 848326
* Bruno Cotrim — RA 848454
* Augusto Senegalia — RA 848116
* Leonardo Moisés — RA 848456

## Repositório GitHub

https://github.com/jorginhoolv123/Projeto-Redes-Neurais-DIOE

---

# Objetivo

Explorar o portal do Diário Oficial Eletrônico de Avaré (DIOE) e desenvolver um pipeline de coleta, processamento e preparação dos dados para utilização em modelos de Inteligência Artificial utilizando Python e PyTorch.

---

# Fonte utilizada

https://imprensaoficialmunicipal.com.br/avare

https://imprensaoficialmunicipal.com.br/listaatos.php?c=Avar%C3%A9&s=Leis

---

# Ferramentas utilizadas

* Python
* requests
* BeautifulSoup
* pandas
* os
* matplotlib
* PyTorch
* scikit-learn
* ChatGPT (OpenAI) — utilizada como apoio na escrita, revisão textual e auxílio no desenvolvimento de código durante o projeto.

---

# Estruturas identificadas

* Publicações organizadas em blocos
* Títulos de matérias
* Possíveis links para documentos (PDFs)
* Datas associadas às publicações

---

# ETAPA 1 — Coleta de dados (Scraping)

## Script desenvolvido

Arquivo:

scraper.py

### Funções implementadas

* Acesso ao portal do DIOE
* Coleta das publicações disponíveis
* Extração de títulos e informações principais
* Geração de dataset inicial

### Execução

python scraper.py

### Resultado

Arquivo gerado:

* diario_avare.csv

Com no mínimo 20 registros coletados.

---

# ETAPA 2 — Processamento e estruturação dos dados

## Script desenvolvido

Uso de Python com pandas para tratamento do dataset coletado.

### Ações realizadas

* Leitura do arquivo diario_avare.csv
* Padronização dos dados em formato estruturado
* Criação de identificador único (ID incremental)
* Conversão do conteúdo textual para formato uniforme
* Geração de nova base tratada

### Arquivo gerado

data/processed/base_textual.csv

### Estrutura final

* id → identificador único
* texto → conteúdo das publicações de leis

### Resultado da Etapa 2

Foi possível estruturar os dados coletados em um formato adequado para processamento computacional, permitindo sua utilização em tarefas de análise textual e aprendizado de máquina.

---

# ETAPA 3 — Processamento de Linguagem Natural (NLP) e Preparação para PyTorch

## Objetivo da Etapa

Preparar os dados textuais para treinamento de modelos de redes neurais, transformando textos em representações numéricas compatíveis com PyTorch.

---

## Análise Exploratória dos Dados (EDA)

Foi realizado um estudo inicial da amostra rotulada através do notebook:

notebooks/03_analise_exploratoria.ipynb

### Análises realizadas

* Distribuição das classes
* Comprimento dos textos
* Frequência das palavras mais utilizadas

A análise permitiu compreender melhor a estrutura dos dados antes do treinamento do modelo.

---

## Pré-processamento e Tokenização

Foi implementado um pipeline de NLP contendo:

* Conversão para letras minúsculas
* Remoção de pontuação
* Remoção de caracteres especiais
* Remoção de palavras irrelevantes (stopwords)
* Separação dos textos em tokens

Exemplo:

Texto original:

"Decreto Municipal nº 4521 - Fica decretado ponto facultativo."

Resultado:

["decreto", "municipal", "fica", "decretado", "ponto", "facultativo"]

---

## Construção do Vocabulário

Foi desenvolvido um processo automático para criação do vocabulário utilizado pelo modelo.

Tokens especiais adicionados:

| Token | Índice |
| ----- | ------ |
| <PAD> | 0      |
| <UNK> | 1      |

Arquivo gerado:

data/processed/vocab.json

---

## Codificação dos Textos

Após a criação do vocabulário, cada publicação foi convertida para uma sequência numérica.

Processos realizados:

* Conversão token → índice
* Padding para textos menores
* Truncamento para textos maiores

Parâmetro utilizado:

max_len = 60

---

## Codificação dos Rótulos

As classes textuais foram convertidas para valores numéricos utilizando Label Encoding.

Exemplo:

* Decreto → 0
* Licitação → 1
* RH → 2

Arquivo gerado:

data/processed/label_map.json

---

## Implementação do Dataset PyTorch

Foi criada a classe:

src/dataset.py

Responsável por:

* Carregar os textos
* Converter tokens em índices
* Aplicar padding e truncamento
* Retornar tensores compatíveis com PyTorch

Métodos implementados:

* **init**()
* **len**()
* **getitem**()

---

## Teste com DataLoader

Foi realizado um teste utilizando DataLoader do PyTorch.

Configuração utilizada:

* batch_size = 8
* shuffle = True

Resultado obtido:

torch.Size([8, 60])

torch.Size([8])

O teste confirmou que o Dataset encontra-se pronto para utilização no treinamento do modelo.

---

## Arquivos Gerados na Etapa 3

* notebooks/03_analise_exploratoria.ipynb
* data/processed/vocab.json
* data/processed/label_map.json
* src/dataset.py

---

# Conclusão

Ao longo das três etapas foi possível realizar a coleta, tratamento e preparação dos dados extraídos do Diário Oficial Eletrônico de Avaré.

Inicialmente foram coletadas as publicações do portal, posteriormente os dados foram estruturados e padronizados, e por fim foram aplicadas técnicas de Processamento de Linguagem Natural (NLP) para transformar os textos em representações numéricas compatíveis com PyTorch.

Com isso, o projeto encontra-se preparado para a Etapa 4, na qual será realizado o treinamento e avaliação de modelos de redes neurais para classificação automática das publicações.
