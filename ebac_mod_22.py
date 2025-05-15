import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')
print(df.head(20).to_string())

#Gráficos de Histograma
plt.figure(figsize=(10, 6))
plt.hist(df['Nota'], bins=100, color="#f5d442", alpha=0.8)
plt.title("Histograma - Notas")
plt.xlabel('Nota')
plt.ylabel('-')
plt.grid(True)
plt.show()

# plt.figure(figsize=(10, 6))
# plt.hist(df['Preço'], bins=100, color="#f5d442", alpha=0.8)
# plt.title("Histograma - Preço")
# plt.xlabel('Preço')
# plt.ylabel('-')
# plt.grid(True)
# plt.show()

#Gráfico de Dispersão
sns.jointplot(x = 'Preço', y='Qtd_Vendidos_Cod', data=df, kind='scatter')
plt.show()

#Mapa de calor
corr = df[['Preço', 'Qtd_Vendidos_Cod']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Temporada e Quantidade de Vendas')
plt.show()

#Gráfico de barra
plt.figure(figsize=(10, 8))
df['Gênero'].value_counts().plot(kind='bar', color='#145e61')
plt.title('Divisão de Genero')
plt.xlabel('Genero')
plt.ylabel('Quantidade')
plt.xticks(rotation=90)
plt.show()

#Gráfico de Pizza
# x = df['Gênero'].value_counts().index
# y = df['Gênero'].value_counts().values
#
# plt.figure(figsize=(10,6))
# plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
# plt.title('Distribuição de Gênero')
# plt.show()


contagem_generos = df['Gênero'].value_counts()

top_n = 5

genero_top = contagem_generos[:top_n]
outros = contagem_generos[top_n:].sum()

valores = list(genero_top.values) + [outros]
labels = list(genero_top.index) + ['Outros']

plt.figure(figsize=(8, 8))
plt.pie(valores, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Distribuição de Gêneros (Top 5 + Outros)')
plt.axis('equal')
plt.show()

#Gráfico de Densidade
plt.figure(figsize=(10, 8))
sns.kdeplot(df['Preço'], fill=True, color='#0aa330')
plt.title('Densidade de Preços')
plt.xlabel('Preços')
plt.show()

#Gráfico de Regressão
sns.regplot(x= 'Preço', y='Qtd_Vendidos_Cod', data=df, color='#a30a19', scatter_kws={'alpha': 0.5, 'color': '#240205'})
plt.title("Regressão de preço por quantidade de vendas")
plt.xlabel('Preço')
plt.ylabel('Qtd de Vendas')
plt.show()