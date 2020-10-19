#2. REVISÃO MODULO 3 - VISUALIZAÇÃO DE DADOS

import matplotlib.pyplot as plt                     # IMPORTA BIBLIOTECA MATPLOTLIB

data = ['set','ago','jul']                          # CRIA UMA LISTA COM OS MESES 
print(saldo_lista)                                  # IMPRIME A LISTA COM OS TRES SALDOS(EX ANTERIOR)
print(data)                                         # IMPRIME A LISTA DE DATA 

plt.plot(data,saldo_lista)                          # IMPRIME O GRAFICO DE LINHA TENDO EIXO X A DATA E EIXO Y O SALDO_LISTA
plt.show()                                          # COMANDO PARA EXIBIR O GRAFICO
