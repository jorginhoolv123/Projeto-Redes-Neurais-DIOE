import pandas as pd

classes = ["RH", "Licitacao", "Decreto"]

dados = []

for i in range(1, 41):

    if i % 3 == 1:
        texto = "Nomeação de servidor"
        classe = "RH"

    elif i % 3 == 2:
        texto = "Contratação de empresa"
        classe = "Licitacao"

    else:
        texto = "Decreto municipal"
        classe = "Decreto"

    dados.append({
        "id": i,
        "texto": texto,
        "classe": classe
    })

df = pd.DataFrame(dados)

df.to_csv(
    "data/processed/amostra_rotulada.csv",
    index=False,
    encoding="utf-8-sig"
)

print("amostra_rotulada.csv criado com 40 registros!")