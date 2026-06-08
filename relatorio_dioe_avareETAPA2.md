# RELATÓRIO DE EXPLORAÇÃO DA FONTE — DIOE AVARÉ

## Integrantes

Grupo:

Jorge Augusto — RA 848435
Adrian Soares — RA 848326
Bruno Cotrim — RA 848454
Eduardo Kenzo — RA 848345
Demian — RA 848341
Augusto Senegalia — RA 848116
Leonardo Moisés — RA 848456

Repositório GitHub:
https://github.com/jorginhoolv123/Projeto-Redes-Neurais-DIOE

## Objetivo

Explorar o portal do Diário Oficial Eletrônico de Avaré (DIOE) e desenvolver um pipeline de coleta e processamento de dados em Python.

## Fonte utilizada

https://imprensaoficialmunicipal.com.br/avare
https://imprensaoficialmunicipal.com.br/listaatos.php?c=Avar%C3%A9&s=Leis

## Ferramentas utilizadas
Python
requests
BeautifulSoup
pandas
os
ChatGPT (OpenAI) — utilizada como apoio na escrita, revisão textual e auxílio no desenvolvimento de código durante o projeto.

## Estrutara identificadas

Publicações organizadas em blocos
Títulos de matérias
Possíveis links para documentos (PDFs)
Datas associadas às publicações
ETAPA 1 — Coleta de dados (Scraping)
Script desenvolvido

Arquivo: scraper.py

Funções implementadas:
Acesso ao portal do DIOE
Coleta das publicações disponíveis
Extração de títulos e informações principais
Geração de dataset inicial
Execução
python scraper.py
Resultado

Arquivo gerado:

diario_avare.csv (mínimo de 20 registros coletados)

## Estrutara identificadas Etapa 2

ETAPA 2 — Processamento e estruturação dos dados
Script desenvolvido

Uso de Python com pandas para tratamento do dataset coletado.

Ações realizadas:
Leitura do arquivo diario_avare.csv
Padronização dos dados em formato estruturado
Criação de identificador único (ID incremental)
Conversão do conteúdo textual para formato uniforme
Geração de nova base tratada
Arquivo gerado
data/processed/base_textual.csv

## Estrutura final

id → identificador único
texto → conteúdo das publicações de leis

## Conclusão

Foi possível realizar com sucesso a coleta inicial de dados do Diário Oficial Eletrônico de Avaré e, na etapa seguinte, estruturar e organizar as informações em um formato adequado para análise e processamento futuro.

O pipeline desenvolvido permite evolução para etapas de NLP, classificação de textos ou análise de publicações oficiais.