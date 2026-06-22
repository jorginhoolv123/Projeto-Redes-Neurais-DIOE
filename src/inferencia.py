import os
import json
import re
import torch

from src.model import DiarioClassifier

MAX_LEN = 60

STOPWORDS = {
    'de','da','do','das','dos','e','o','a',
    'os','as','para','no','na','nos','nas',
    'que','em','um','uma','com','por'
}

def tokenizar(texto):
    texto = texto.lower()
    texto = re.sub(r'[^a-zà-ú\s]', ' ', texto)
    tokens = texto.split()

    return [
        t for t in tokens
        if t not in STOPWORDS and len(t) > 1
    ]


# Caminho da raiz do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Carrega vocabulário
with open(os.path.join(BASE_DIR, "data", "processed", "vocab.json"), "r", encoding="utf8") as f:
    vocab = json.load(f)

# Carrega mapa de classes
with open(os.path.join(BASE_DIR, "data", "processed", "label_map.json"), "r", encoding="utf8") as f:
    label_map = json.load(f)

id2label = {v: k for k, v in label_map.items()}

# Cria modelo
modelo = DiarioClassifier(
    vocab_size=len(vocab),
    num_classes=len(label_map)
)

# Carrega pesos treinados
modelo.load_state_dict(
    torch.load(
        os.path.join(BASE_DIR, "models", "modelo.pt"),
        map_location="cpu"
    )
)

modelo.eval()


def codificar(texto):

    tokens = tokenizar(texto)

    ids = [vocab.get(token, 1) for token in tokens]

    ids = ids[:MAX_LEN]

    while len(ids) < MAX_LEN:
        ids.append(0)

    return torch.tensor([ids], dtype=torch.long)


def prever(texto):

    x = codificar(texto)

    with torch.no_grad():

        saida = modelo(x)

        classe = torch.argmax(saida, dim=1).item()

    return id2label[classe]


if __name__ == "__main__":

    texto = input("Digite um texto: ")

    print("Classe prevista:", prever(texto))