import torch
import torch.nn as nn


class DiarioClassifier(nn.Module):
    """
    Modelo:
    Embedding
        ↓
    Média dos vetores
        ↓
    Linear
        ↓
    ReLU
        ↓
    Dropout
        ↓
    Linear
    """

    def __init__(
        self,
        vocab_size,
        num_classes,
        embedding_dim=128,
        hidden_dim=128,
        padding_idx=0
    ):
        super().__init__()

        self.embedding = nn.Embedding(
            num_embeddings=vocab_size,
            embedding_dim=embedding_dim,
            padding_idx=padding_idx
        )

        self.fc1 = nn.Linear(
            embedding_dim,
            hidden_dim
        )

        self.relu = nn.ReLU()

        self.dropout = nn.Dropout(0.3)

        self.fc2 = nn.Linear(
            hidden_dim,
            num_classes
        )

    def forward(self, x):

        emb = self.embedding(x)

        mask = (x != 0).unsqueeze(-1)

        emb = emb * mask

        soma = emb.sum(dim=1)

        tamanho = mask.sum(dim=1).clamp(min=1)

        media = soma / tamanho

        x = self.fc1(media)

        x = self.relu(x)

        x = self.dropout(x)

        x = self.fc2(x)

        return x