import pandas as pd
import json

from torch.utils.data import DataLoader

from dataset import DiarioDataset

df = pd.read_csv(
    "data/processed/amostra_rotulada.csv"
)

with open(
    "data/processed/vocab.json",
    encoding="utf-8"
) as f:
    vocab = json.load(f)

with open(
    "data/processed/label_map.json",
    encoding="utf-8"
) as f:
    label2id = json.load(f)

dataset = DiarioDataset(
    df,
    vocab,
    label2id
)

loader = DataLoader(
    dataset,
    batch_size=8,
    shuffle=True
)

x, y = next(iter(loader))

print(x.shape)
print(y.shape)