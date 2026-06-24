import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#Carrega os dados
df = pd.read_csv("dados_bcb.csv")

#CONFIGURAÇÕES DE ESTILO
sns.set(style="darkgrid")
fig, axes = plt.subplots(3, 1, figsize=(12, 18))
fig.suptitle("Indicadores Econômicos Brasil -  Banco Central", 
      fontsize=16, fontweight='bold', y=1.02)

cores = {'Selic': '#2ECC71', 'IPCA': '#E74C3C', 'Dolar': '#3498DB'}

for i, (indicador, cor) in enumerate(cores.items()):
    filtro = df[df['indicador'] == indicador]
    axes[i].plot(filtro['data'], filtro ['valor'], color=cor, linewidth=2, marker='o', markersize=4)
    axes[i].set_title(f"{indicador}", fontsize=13, fontweight='bold')
    axes[i].set_ylabel("Valor")
    axes[i].tick_params(axis='x', rotation=45)

plt. tight_layout()
plt.savefig('dashboard.png', dpi=150, bbox_inches='tight')
print("\n Dashboard salvo como dashboard.png")