import requests

# A API do Banco Central é pública — não precisa de senha
# Código 433 = Taxa Selic | 11426 = IPCA | 1 = USD/BRL
indicadores = {
    "Selic": 432,
    "IPCA": 13522,
    "Dólar": 1
}

for nome, codigo in indicadores.items():
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados/ultimos/12?formato=json"
    
    resposta = requests.get(url)
    dados = resposta.json()
    
    print(f"\n📊 {nome} — últimos 12 registros:")
    for item in dados:
        print(f"  Data: {item['data']} | Valor: {item['valor']}")
