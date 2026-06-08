import pandas as pd
import os

df = pd.read_csv("diario_avare.csv")

coluna_texto = df.columns[0]

base = pd.DataFrame({
    "id": range(1, len(df) + 1),
    "texto": df[coluna_texto].astype(str)
})

os.makedirs("data/processed", exist_ok=True)

base.to_csv(
    "data/processed/base_textual.csv",
    index=False,
    encoding="utf-8-sig"
)

print("base_textual.csv criado com sucesso!")