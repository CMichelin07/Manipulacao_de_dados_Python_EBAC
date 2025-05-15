import pymysql
import pandas as pd
from sqlalchemy import create_engine

def conexao_mysql(host, user, password, db, table):
    # Criar conexão
    conn = pymysql.connect(host=host, user=user, password=password, db=db)
    cursor = conn.cursor()

    # Executar consulta
    query = "SELECT * FROM " + table + " LIMIT 10"
    cursor.execute(query)

    # Buscar resultados
    resultados = cursor.fetchall()

    # Exibir os resultados
    print("Tabela MySQL:")
    for linha in resultados:
        print(linha)

    # Fechar a conexao
    cursor.close()
    conn.close()

def df_conexao_mysql(host, user, password, db, table):
    # Criar conexao
    conn = pymysql.connect(host=host, user=user, password=password, db=db)

    # Executar consulta e salvar em um DataFrame
    query = "SELECT * FROM " + table
    df = pd.read_sql(query, conn)

    # Exibir resultados
    print("Tabela MySQL com DataFrame: \n", df.head())

    # Fechar conexao
    conn.close()
    return df

def conexao_excel(path):
    # Ler arquivo Excel
    df = pd.read_excel(path)

    # Escrever arquivo CSV
    df.to_csv("dados.csv", index=False)

def conexao_csv(path):
    # Ler arquivo CSV
    df = pd.read_csv(path)
    print("Dados CSV: \n", df.head())

    # Escrever arquivo JSON
    df.to_json("dados.json", orient="records", index=False)

# Executando funções
conexao_mysql(host="localhost", user="root", password="21071023", db="loja_informatica", table="cliente")

df_cliente = df_conexao_mysql("localhost", "root", "root", "loja_informatica", "cliente")
# df_cliente.to_excel("dados.xlsx", index=False)

# conexao_excel("dados.xlsx")
# conexao_csv("dados.csv")
