GRAFICO DE BARRAS - MODO 2 DE FAZER
 
df.plot(x='Estação', y='Entradas', kind = 'bar')
plt.title('Estações - Fluxo')
plt.xlabel('Estações')
plt.ylabel('Valores')
plt.show()
 
 
 
GRAFICO DE BARRAS - MODO 1 DE FAZER
 
plt.bar('Estação','Entradas', data = df)
plt.title('Estações - Fluxo')
plt.xlabel('Estações')
plt.ylabel('Valores')
plt.show()
