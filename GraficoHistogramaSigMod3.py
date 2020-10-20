# MODO 1 FAZER HISTOGRAMA
plt.hist('Custo da Unidade', data = df,bins = 8 , density=True)
plt.title('Histigrama Custo Unidade')
plt.show()

 # MODO 2 DE FAZER HISTOGRAMA

df['Custo da Unidade'	].hist()
plt.show()
