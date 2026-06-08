import pandas as pd

df = pd.read_csv("data/processed/base_textual.csv")

palavras_ruins = [
    "economia de recursos",
    "árvores salvas",
    "acesso rápido",
    "filtro por data"
]

for palavra in palavras_ruins:
    df = df[~df["texto"].str.lower().str.contains(palavra, na=False)]

df["texto"] = (
    df["texto"]
    .astype(str)
    .str.lower()
    .str.strip()
)

df.to_csv(
    "data/processed/base_textual.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Base textual limpa!")