import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# TO-DO: eliminar os comentários "Por Josségio" e ajustar o código

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

# Visualizar as primeiras linhas do DataFrame
print(df.head())

print('---------------------------------------------------------------------------------------')

# Remover linhas com valores nulos
df.dropna(inplace=True)

# Remover duplicatas
df.drop_duplicates(inplace=True)

# Verificar informações sobre os dados
print(df.info())

print('---------------------------------------------------------------------------------------')

# Estatísticas descritivas
print(df.describe())

print('---------------------------------------------------------------------------------------')

# Ver distribuição de uma coluna
print(df['coluna_de_interesse'].value_counts())

print('---------------------------------------------------------------------------------------')

# Exemplo de gráfico de barras
sns.barplot(x='coluna_x', y='coluna_y', data=df)
plt.show()

# Exemplo de histograma
df['coluna_de_interesse'].hist()
plt.show()

# Matriz de correlação
correlacao = df.corr()
print(correlacao)

print('---------------------------------------------------------------------------------------')

# Mapa de calor da correlação
sns.heatmap(correlacao, annot=True, cmap='coolwarm')
plt.show()

