ETAPA 4 — Treinamento, Avaliação e Interface da Aplicação
Objetivo da Etapa

Desenvolver um modelo de rede neural utilizando PyTorch para classificar automaticamente publicações do Diário Oficial de Avaré, avaliando seu desempenho e disponibilizando uma interface simples para realização de previsões.

Modelo de Rede Neural

Foi implementado o arquivo:

src/model.py

O modelo desenvolvido possui a seguinte arquitetura:

Camada Embedding para representação vetorial das palavras;
Cálculo da média dos vetores (Mean Pooling);
Camada Linear totalmente conectada;
Função de ativação ReLU;
Camada Dropout para reduzir overfitting;
Camada Linear de saída responsável pela classificação.

Arquitetura utilizada:

Entrada
      ↓
Embedding
      ↓
Média dos Embeddings
      ↓
Linear
      ↓
ReLU
      ↓
Dropout
      ↓
Linear
      ↓
Classe Prevista
Treinamento do Modelo

O treinamento foi realizado através do notebook:

notebooks/04_treinamento_avaliacao.ipynb

Configurações utilizadas:

Framework: PyTorch
Função de perda: CrossEntropyLoss
Otimizador: Adam
Learning Rate: 0.001
Batch Size: 16
Número de épocas: 20

Durante o treinamento foi registrada a evolução da função de perda (Loss), permitindo acompanhar a aprendizagem do modelo.

Curva de Aprendizado

Foi gerado um gráfico demonstrando a redução da Loss ao longo das épocas.

Arquivo gerado:

docs/curva_aprendizado.png

Observou-se redução contínua da perda durante o treinamento, indicando convergência do modelo.

Avaliação do Modelo

Após o treinamento, o modelo foi avaliado utilizando o conjunto de teste separado automaticamente pelo algoritmo.

As métricas calculadas foram:

Acurácia
Precision
Recall
F1-Score
Matriz de Confusão

Essas métricas permitiram avaliar a capacidade do modelo em identificar corretamente cada categoria de publicação.

Matriz de Confusão

Foi gerada uma matriz de confusão contendo as previsões corretas e incorretas para cada classe.

A análise demonstrou bom desempenho do classificador, com predominância de acertos nas três categorias utilizadas:

Decreto
Licitação
RH
Função de Inferência

Foi implementado o arquivo:

src/inferencia.py

Essa função realiza:

carregamento do modelo treinado;
carregamento do vocabulário;
tokenização do texto informado;
codificação para índices numéricos;
execução da rede neural;
retorno da classe prevista.

Exemplo de utilização:

Digite um texto:

"Fica homologado o processo licitatório..."

Resultado:

Classe prevista:
Licitação
Interface da Aplicação

Foi desenvolvida uma interface utilizando Streamlit.

Arquivo:

app.py

A aplicação permite que o usuário digite um trecho de uma publicação do Diário Oficial e receba automaticamente a categoria prevista pelo modelo.

Fluxo da aplicação:

Texto digitado
        ↓
Pré-processamento
        ↓
Rede Neural
        ↓
Classe Prevista
Arquivos Gerados na Etapa 4
src/model.py
src/inferencia.py
app.py
notebooks/04_treinamento_avaliacao.ipynb
docs/curva_aprendizado.png
models/modelo.pt
Conclusão Final

Ao longo das quatro etapas do projeto foi desenvolvido um sistema completo para classificação automática de publicações do Diário Oficial Eletrônico de Avaré.

Inicialmente foram coletados os dados por meio de técnicas de Web Scraping. Em seguida, os textos passaram por etapas de limpeza, organização e preparação utilizando técnicas de Processamento de Linguagem Natural (NLP). Posteriormente, foi construída uma base estruturada compatível com o PyTorch, permitindo o treinamento de uma rede neural para classificação das publicações.

Na etapa final foi implementado um modelo baseado em Embedding e camadas lineares, treinado utilizando o otimizador Adam e a função de perda CrossEntropyLoss. O modelo foi avaliado por meio de métricas como acurácia, precisão, recall, F1-Score e matriz de confusão, apresentando bom desempenho na identificação das classes Decreto, Licitação e RH.

Por fim, foi desenvolvida uma interface utilizando Streamlit, permitindo que qualquer usuário insira um trecho de texto e obtenha automaticamente a classificação prevista pelo modelo treinado.

O projeto atingiu os objetivos propostos, integrando técnicas de raspagem de dados, processamento de linguagem natural, aprendizado profundo e desenvolvimento de aplicações, resultando em uma solução funcional para classificação automática de documentos do Diário Oficial.