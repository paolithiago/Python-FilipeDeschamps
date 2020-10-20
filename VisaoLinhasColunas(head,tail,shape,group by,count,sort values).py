# ACESSAR ATRAVES DO PANDA O AQUIVO CONTROLE DA EMPRESA EXCEL
df = pd.read_excel('/content/gdrive/My Drive/ComPython/controle_da_empresa.xlsx')                           # CARREGA O DATASET

print('__________________________________ANALISE LINHAS COLUNAS_________________________')
print('Quantidade de Linhas:',df.shape[0])                                                                  # ANALISE QTDE DE LINHAS
print('Quantidade de Colunas',df.shape[1])                                                                  # ANALISE QTDE DE COLUNAS
print('Media Estoque Minimo',df['Estoque Mínimo'].mean())                                                   # MEDIA NO ESTOQUE MINIMO
print('Media Custo da Unidade',df['Custo da Unidade'].mean())                                               # MEDIA DO CUSTO DA UNIDADE
print('Media Preço da Unidade',df['Preço da Unidade'].mean())                                               # MEDIA DO PREÇO DA UNIDADE
print('Media Estoque Atual', df['Estoque Atual'].mean())                                                    # MEDIA ESTOQUE ATUAL    
total = df['Estoque Atual'].sum()                                                                           # TOTAL QUANTIDADE EM ESTOQUE
Val_Estoque_Item = (df.groupby('Item')['Estoque Atual'].sum().sort_values(ascending = False))               # CALCULO DOS VALORES DO ESTOQUE VISTOS POR ITEM -VAI PARA VARIAVEL    
Taxa_Estoque_Item = (Val_Estoque_Item/total)*100                                                            # CALCUA TAXA DO ESTOQUE POR CADA ITEM PELO TOTAL PARA GERAR %  
print('________________________________ANALISE SITUACAO ESTOQUE POR ITEM_______________')
print(Val_Estoque_Item)                                                                                     # IMPRIME ESTOQUE POR ITEM
print('________________________________ANALISE SITUACAO ESTOQUE %______________________')
print(Taxa_Estoque_Item)                                                                                    # IMPRIME O 5 EM ESTOQUE PELO ITEM
print('________________________________ANALISE INCIDENCIA DE ITENS______________________________')
print((df['Item'].value_counts()/df.shape[0])*100)                                                          # CALCULA INCIDENCIA POR ITEM
