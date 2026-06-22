import json
import re
import torch

from torch.utils.data import Dataset

STOPWORDS = {
    'de','da','do','das','dos','e','o','a',
    'os','as','para','no','na','nos','nas',
    'que','em','um','uma','com','por'
}

MAX_LEN = 60

def tokenizar(texto):

    texto = texto.lower()

    texto = re.sub(
        r'[^a-zà-ú\s]',
        ' ',
        texto
    )

    tokens = texto.split()

    return [
        t
        for t in tokens
        if t not in STOPWORDS and len(t) > 1
    ]

class DiarioDataset(Dataset):

    def __init__(
        self,
        dataframe,
        vocab,
        label2id,
        max_len=MAX_LEN
    ):

        self.textos = dataframe["texto"].tolist()

        self.rotulos = dataframe["classe"].tolist()

        self.vocab = vocab

        self.label2id = label2id

        self.max_len = max_len

    def __len__(self):
        return len(self.textos)

    def codificar(self, texto):

        tokens = tokenizar(texto)

        ids = [
            self.vocab.get(token, 1)
            for token in tokens
        ]

        ids = ids[:self.max_len]

        ids += [0] * (
            self.max_len - len(ids)
        )

        return ids

    def __getitem__(self, idx):

        x = torch.tensor(
            self.codificar(
                self.textos[idx]
            ),
            dtype=torch.long
        )

        y = torch.tensor(
            self.label2id[
                self.rotulos[idx]
            ],
            dtype=torch.long
        )

        return x, y