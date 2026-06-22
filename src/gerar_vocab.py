import pandas as pd
import json
import re
from collections import Counter

STOPWORDS = {
    'de','da','do','das','dos','e','o','a',
    'os','as','para','no','na','nos','nas',
    'que','em','um','uma','com','por'
}

def tokenizar(texto):
    texto = texto.lower()
    texto = re.sub(r'[^a-zà-ú\s]', ' ', texto)

    tokens = texto.split()

    tokens = [
        t for t in tokens
        if t not in STOPWORDS and len(t) > 1
    ]

    return tokens

df = pd.read_csv("data/processed/amostra_rotulada.csv")

contador = Counter()

for texto in df["texto"]:
    contador.update(tokenizar(texto))

vocab = {
    "<PAD>":0,
    "<UNK>":1
}

for token, freq in contador.items():
    if freq >= 1:
        vocab[token] = len(vocab)

with open(
    "data/processed/vocab.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        vocab,
        f,
        ensure_ascii=False,
        indent=4
    )

print("Vocabulário salvo.")
print("Tamanho:", len(vocab))