import pandas as pd
import numpy as np

# Caminho do arquivo
caminho_arquivo = r'D:\para_edson\dados.csv'

# Lê os dados do arquivo CSV
df = pd.read_csv(caminho_arquivo)

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
