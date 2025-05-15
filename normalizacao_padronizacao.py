import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv("clientes-v2-tratados.csv")

print (df.head())

df = df.drop(labels=['data', 'estado', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao'], axis=1)

#Normalização - MinMaxScaler
scaler = MinMaxScaler()
df['idadeMinMaxscaler'] = scaler.fit_transform(df[['idade']])
df['salarioMinMaxscaler'] = scaler.fit_transform(df[['salario']])

min_max_scaler = MinMaxScaler(feature_range=(-1, 1))
df['idadeMinMaxscaler_mm'] = min_max_scaler.fit_transform(df[['idade']])
df['salarioMinMaxscaler_mm'] = min_max_scaler.fit_transform(df[['salario']])

#Padronização - StandardScaler
scaler = StandardScaler()
df['idadeStandardScaler'] = scaler.fit_transform(df[['idade']])
df['salarioStandardScaler'] = scaler.fit_transform(df[['salario']])

#Padronização - RobustScaler
scaler = RobustScaler()
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']])
df['salarioRobustScaler'] = scaler.fit_transform(df[['salario']])

print(df.head(15))

print("MinMaxScaler (De 0 a 1):")
print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(df['idadeMinMaxscaler'].min(), df['idadeMinMaxscaler'].max(), df['idadeMinMaxscaler'].mean(), df['idadeMinMaxscaler'].std()))
print("Salario - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(df['salarioMinMaxscaler'].min(), df['salarioMinMaxscaler'].max(), df['salarioMinMaxscaler'].mean(), df['salarioMinMaxscaler'].std()))

print("\nMinMaxScaler (De -1 a 1)")
print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(df['idadeMinMaxscaler_mm'].min(), df['idadeMinMaxscaler_mm'].max(), df['idadeMinMaxscaler_mm'].mean(), df['idadeMinMaxscaler_mm'].std()))
print("Salario - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(df['salarioMinMaxscaler_mm'].min(), df['salarioMinMaxscaler_mm'].max(), df['salarioMinMaxscaler_mm'].mean(), df['salarioMinMaxscaler_mm'].std()))

print("\nStandardScaler (Ajuste a Média a 0 e desvio padrão a 1): ")
print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.18f} Std: {:.4f}".format(df['idadeStandardScaler'].min(), df['idadeStandardScaler'].max(), df['idadeStandardScaler'].mean(), df['idadeStandardScaler'].std()))
print("Salario - Min: {:.4f} Max: {:.4f} Mean: {:.18f} Std: {:.4f}".format(df['salarioStandardScaler'].min(), df['salarioStandardScaler'].max(), df['salarioStandardScaler'].mean(), df['salarioStandardScaler'].std()))

print("\nRobustScaler (Ajuste a mediana e IQR):")
print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(df['idadeRobustScaler'].min(), df['idadeRobustScaler'].max(), df['idadeRobustScaler'].mean(), df['idadeRobustScaler'].std()))
print("Salario - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(df['salarioRobustScaler'].min(), df['salarioRobustScaler'].max(), df['salarioRobustScaler'].mean(), df['salarioRobustScaler'].std()))