import pandas as pd
import numpy as np


# TO-DO: eliminar os comentários "Por Josségio" e ajustar o código
"""
# Caminho do arquivo
caminho_arquivo = r'D:\para_edson\dados.csv'
""" # TO-DO: retirar, pois foi ajustado pelo código abaixo

import os # Por Jossérgio

# Carregar um arquivo CSV

# Por Jossérgio
# Checa se o arquivo existe
# TO-DO: Jogar como parâmetro em linha de comando
ARQUIVO = "/home/usuario/para_edson/dhav2.csv"
if os.path.exists (ARQUIVO):
    df = pd.read_csv(ARQUIVO)
else:
    print (f"Arquivo {ARQUIVO} não localizado!")
    quit (1)

# Função para verificar se o período está no DataFrame
def verificar_periodo(df, data_inicio, data_fim):
    # Convertemos as datas de entrada em formato datetime
    data_inicio = pd.to_datetime(data_inicio)
    data_fim = pd.to_datetime(data_fim)
    
    # Verificamos se o intervalo solicitado existe no DataFrame
    if (df['data'] >= data_inicio).any() and (df['data'] <= data_fim).any():
        # Filtra os dados dentro do intervalo
        periodo_filtrado = df[(df['data'] >= data_inicio) & (df['data'] <= data_fim)]
        if not periodo_filtrado.empty:
            return periodo_filtrado
        else:
            return f"Período {data_inicio} a {data_fim} não encontrado."
    else:
        # Verificamos o motivo: intervalo fora do range de datas no DataFrame
        min_data, max_data = df['data'].min(), df['data'].max()
        if data_inicio < min_data:
            return f"A data de início {data_inicio} é anterior à menor data disponível {min_data}."
        elif data_fim > max_data:
            return f"A data de fim {data_fim} é posterior à maior data disponível {max_data}."
        else:
            return "Período não encontrado."

# Exemplo de uso da função
data_inicio = '2023-01-03'
data_fim = '2023-01-06'

resultado = verificar_periodo(df, data_inicio, data_fim)
print(resultado)
