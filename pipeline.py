import requests
import pandas as pd

indicadores = {
    "Selic": 432,
    "IPCA": 13522,
    "Dolar": 1
}

todos_os_dados = []

for nome, codigo in indicadores.items():
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados/ultimos/12?formato=json"
    
    resposta = requests.get(url)
    dados = resposta.json()
    
    for item in dados:
        if isinstance(item, dict):
            todos_os_dados.append({
                "indicador": nome,
                "data": item.get("data", ""),
                "valor": float(item.get("valor", 0))
            })
    
    print(f"✅ {nome} — {len(dados)} registros coletados")

df = pd.DataFrame(todos_os_dados)
df.to_csv("dados_bcb.csv", index=False)

print("\n📁 Arquivo dados_bcb.csv criado!")
print(df.head(10))