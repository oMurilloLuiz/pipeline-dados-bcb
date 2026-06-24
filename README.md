# 📊 Pipeline ETL — Indicadores Econômicos do Brasil

Pipeline de dados desenvolvido em Python que extrai, transforma e carrega 
indicadores econômicos em tempo real via API pública do Banco Central do Brasil.

## 🚀 Tecnologias utilizadas
- Python 3.x
- Pandas
- Requests
- API pública do Banco Central (SGS/BCB)

## 📈 Indicadores coletados
| Indicador | Fonte | Frequência |
|-----------|-------|------------|
| Taxa Selic | Banco Central | Diária |
| IPCA | Banco Central | Mensal |
| Dólar (USD/BRL) | Banco Central | Diária |

## ⚙️ Como executar
```bash
# Clone o repositório
git clone https://github.com/oMurilloLuiz/pipeline-dados-bcb.git

# Instale as dependências
pip install requests pandas

# Execute o pipeline
python pipeline.py


## 📁 Estrutura do projeto

## 👨‍💻 Autor
**Murillo Luiz Vieira da Silva**  
[LinkedIn](https://www.linkedin.com/in/murillo-luiz) · 
[GitHub](https://github.com/oMurilloLuiz)