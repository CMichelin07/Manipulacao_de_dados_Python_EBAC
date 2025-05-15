import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Exemplo: Criação de um gráfico de dispersão com Matplotlib e Seaborn

# Dados de exemplo
data = {
    'idade': [23, 45, 56, 25, 34, 42, 67, 29, 38, 50],
    'salario': [50000, 80000, 120000, 45000, 60000, 75000, 130000, 48000, 70000, 90000]
}
df = pd.DataFrame(data)

# Gráfico de dispersão com Matplotlib
plt.figure(figsize=(10, 6))
plt.scatter(df['idade'], df['salario'], color='blue', alpha=0.5)
plt.title('Relação entre Idade e Salário')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.show()

# Gráfico de dispersão com Seaborn
plt.figure(figsize=(10, 6))
sns.scatterplot(x='idade', y='salario', data=df, hue='idade', palette='viridis')
plt.title('Relação entre Idade e Salário')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.show()
