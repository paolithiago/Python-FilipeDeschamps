#https://colab.research.google.com/drive/17HaeRH-ZtgUgxGdDH37C-tSpnFBFrTql#scrollTo=prR1dE_CXlDl
# importando o pandas
import pandas as pd

  
#________________________________ BLOCO TREINAMETO ______________________________________________________________
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

#_________________ ANALISE VALORES DUPLICADOS __________________________________________________________________________
df.duplicated() # NESTE CASO GEREI O DUPLICATED PARA TODAS AS LINHAS 100% ENTAO TEMOS A LINHA 7 DUPLICADA.  ANALISANDO O BASE, A LINHA 7 E EXATAMENTE IGUAL A LINHA 6
df.duplicated(subset = 'codigo_pagamento') # AGORA A ANALISE E SOBRE A COLUNA CODIGO PAGAMENTO, SOMENTE A UNICA COLUNA, O QUE ENTENDE E QUE TEMOS MAIS DE UM PAGAMENTO COM O MESMO CODIGO DE BARRAS

# NESTE CASO REMOVEMOS A LINHA QUE ESTAVA 100% DUPLICADA

df.drop_duplicates(inplace=True)
df.duplicated()

# NESTE CASO USANDO O DROP DUPLICATES COM SUBSET E INPLACE REMOVEMOS AS LINHAS QUE TINHAM O CODIGO DE BARRAR DUPLICADOS, E NAO 100% D LINHA
df.drop_duplicates(subset='codigo_pagamento', inplace=True)
df.drop_duplicates
