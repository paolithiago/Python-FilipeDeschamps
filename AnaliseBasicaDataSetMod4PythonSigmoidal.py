# importando o pandas
import pandas as pd

df = pd.read_excel('https://www.dropbox.com/s/v0x8mbaygdqubli/contas_a_pagar.xlsx?dl=1')
df.head()                       # EXTRAI LINHAS DO DATASET
df                              # EXTRAI OS VALORES DO DATASET
df.groupby('pagamento')['valor'].sum().sort_values(ascending = False)           #GERA ANALISE DE SOMA DE GASTOS POR TIPO DE PAGAMENTO
df['codigo_pagamento'].value_counts()                                           # ORDENA A CONTAGEM DE VALORES POR CODIGO DE PAGAMENTO - TEMOS VALORES DUPLICADOS
df['pagamento'].unique()                                                        # EXTRAI OS VALORES UNICOS DE UMA COLUNA
df['valor'].sum()                                                               # SOMA UMA COLUNA
print("Quantidade de Linhas do Dataset",df.shape[0])                            # VERIFICA O TAMANHO DE LINHAS DO DATASET
print("Quantidade de colunas do DataSet",df.shape[1])                           # VERIFICA O TAMANHO DE COLUNAS DO DATASET
df['pagamento'] = df['pagamento'].apply(lambda x:x.capitalize())                # COLOCA A PRIMEIRA LETRA DE CADA PALAVRA DE CADA LINHA DA COLUNA PAGAMENTO MAIUSUCLA
df
analidupli = df[df['pagamento']=='Segurança']                                  # CRIA UM OBJETO ESPECIFICI SOMENTE COM VALORES DA COLUNA PAGAMENTO ONDE VALORES = SEGURNAÇA - ANALISE MELHOR     
analidupli

print(df.isnull().sum())                                                               # VERIFICA SE TEMOS VALORES NULOS POR COLUNA
print(df.isnull().sum().sort_values(ascending = False)/df.shape[0]*100)                # CASOVALORES NULOS, SOMA PARA VER QUANTIDADE POR COLUNA, ORDENA E DIVIDE PELA QTDE DE LINHAS COM MULTP POR 100 PARA TER %
df.groupby('pagamento')['valor'].sum().sort_values(ascending = False).plot.bar()      # IMPRIME UM GRAFICO BASICO COM SOMA DE PAGAMENTO POR TIPO DE VALOR  
df['codigo_pagamento'].value_counts().plot.bar()                                      # IMPRIME UM GRAFICO DE BARRAS COM CONTAGEM DE VALORES POR CODIGO PAGAMENTO MOSTRANDO DUPLICIDADE  
