import pandas as pd
import json

df = pd.read_csv("data/processed/amostra_rotulada.csv")

classes = sorted(df["classe"].unique())

label2id = {
    classe:i
    for i, classe in enumerate(classes)
}

with open(
    "data/processed/label_map.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        label2id,
        f,
        ensure_ascii=False,
        indent=4
    )

print(label2id)