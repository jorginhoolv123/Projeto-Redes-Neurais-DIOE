import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://imprensaoficialmunicipal.com.br/listaatos.php?c=Avar%C3%A9&s=Leis"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

dados = []

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    tabelas = soup.find_all("tr")

    for linha in tabelas:

        colunas = linha.find_all("td")

        if len(colunas) >= 5:

            titulo = colunas[0].get_text(strip=True)
            data = colunas[1].get_text(strip=True)
            edicao = colunas[2].get_text(strip=True)
            ano = colunas[3].get_text(strip=True)

            dados.append({
                "titulo": titulo,
                "data": data,
                "edicao": edicao,
                "ano": ano,
                "tipo": "Lei"
            })

    df = pd.DataFrame(dados)

    df.to_csv(
        "diario_avare.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print(f"{len(df)} registros coletados.")

else:
    print("Erro ao acessar o site.")