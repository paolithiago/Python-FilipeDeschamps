df.groupby('Estação')['Entradas'].sum().sort_values(ascending = False)            # ORDENA VALORES SOMANDO DO MAIOR P/MENOR
df.groupby('Estação')['Entradas'].sum().sort_values(ascending = False).plot.bar() # COM GRAFICO
