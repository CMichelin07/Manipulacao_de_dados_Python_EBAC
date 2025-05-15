import pandas as pd

#Função para calcular um cubo de um número
def eleva_cubo(x):
    return x ** 3

#Expressao de lambda para calcular o cubo de um número
eleva_cubo_lambda = lambda x: x ** 3

print(eleva_cubo(2))
print(eleva_cubo_lambda(2))

df = pd.DataFrame({"numeros" : [1, 2, 3, 4, 5, 10]})

df["cubo_funcao"] = df["numeros"].apply(eleva_cubo)
df["cubo_lambda"] = df["numeros"].apply(lambda x: x ** 3)
print(df)


soma = lambda x, y: x + y
print(soma(3, 5))  # Saída: 8

numeros = [1, 2, 3, 4]
quadrados = list(map(lambda x: x**2, numeros))
print(quadrados)  # Saída: [1, 4, 9, 16]

numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [2, 4, 6]

pessoas = [("Ana", 25), ("Pedro", 19), ("Maria", 30)]
ordenado = sorted(pessoas, key=lambda x: x[1])  # Ordena pela idade
print(ordenado)
# Saída: [('Pedro', 19), ('Ana', 25), ('Maria', 30)]

