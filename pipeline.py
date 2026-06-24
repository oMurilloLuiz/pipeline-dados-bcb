import requests
import pandas as pd

indicadores = {
    "Selic": 432,
    "IPCA": 13522,
    "Dólar": 1
}

todos_os_dados = []

for nome, codigo in indicadores.items():
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados?formato=json"
    response = requests.get(url)
    dados = response.json()
    
    for item in dados:
        todos_os_dados.append({
            "Indicador": nome,
            "Data": item["data"],
            "Valor": float(item["valor"])
    })
        
print(f"{nome} - {len(dados)} registros coletados.")

df = pd.DataFrame(todos_os_dados)
df.to_csv("dados_bcd.csv", index=False)

print("\n Arquivo CSV 'dados_bcd.csv' criado com sucesso!")
print(df.head(10))