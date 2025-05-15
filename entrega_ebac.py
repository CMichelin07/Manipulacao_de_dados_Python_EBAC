import pandas as pd

df = pd.read_csv('/data/ecommerce_ex2.csv')

print(df.head().to_string())
print(df.tail().to_string())
# Escreva seu código abaixo
# Verifique a quantidade de linhas e colunas
linhas_colunas = df.shape
print('Verificar a qtd de Linhas e colunas: ', linhas_colunas)

# Verifique os tipos de dados
tipos = df.dtypes
print('Verificar Tipagem:\n', tipos)

# Verifique a quantidade de valores nulos
nulos = df.isnull().sum()
print('Verificar valores nulos:\n', nulos)

#  Substitua os valores nulos das colunas ‘Temporada’ e ‘Marca’ por ‘Não Definido’
df[['Temporada', 'Marca']] = df[['Temporada', 'Marca']].fillna('Não Definido')

# Converter a coluna 'Marca' para letras minúsculas
df['Marca']= df['Marca'].str.lower()

# Converter a coluna 'Material' para letras minúsculas
df['Material']= df['Material'].str.lower()

# Converter a coluna 'Temporada' para letras minúsculas
df['Temporada']= df['Temporada'].str.lower()


# Remover linhas duplicadas
df = df.drop_duplicates()

# Remover linhas com menos de 8 valores não nulos
# O parâmetro 'thresh' define o número mínimo de valores não nulos necessários para manter a linha
df = df.dropna(thresh=8)

print("Qtd de registros nulos com dropna:", df.isnull().sum().sum())