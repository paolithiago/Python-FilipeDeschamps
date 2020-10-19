#https://colab.research.google.com/drive/1wqUZyVogLcz4fwD2cEhkGYUiIZaMu6rR#scrollTo=HV7gj8ltU73E

TREINO ANALISE CARTAO - SALDO AGO/SET/OUT

!pip install pdfplumber

# IMPORTA BIBLIOTECAS NECESSARIOAS PARA A ANALISE PDF

import pdfplumber
from google.colab import drive
import os

drive.mount('/content/gdrive')                                                    # MONTA O ACESSO AO GOOGLE DRIVE

os.getcwd()                                                                       # VERIFICA QUAL PASTA ESTA
os.chdir('/content/gdrive/My Drive/Trilha de Aprendizado/Python/arquivospdf')     # ALTERA O DIRETORIO DO DRIVE
os.getcwd()                                                                       # VERIFICA QUAL PASTA ESTA


pdfcartao = pdfplumber.open('Bradesco_19102020_103701.pdf')                       # ABRE UM ARQUIVO ESPECIFICO E COLOCA NA VARIAVLE PDFCARTAO
print(pdfcartao.pages)                                                            
pagina2 = pdfcartao.pages[1]                                                      # ESCOLHE UMA PAGINA E COLOCA NA VARIAVEL -ESCOLHA DE ACORDO COM VALOR QUE BUSCA
print(pagina2)
texto2 = pagina2.extract_text()                                                   # EXTRAI O TEXTO DA VARIAVEL PAGINA ESCOLHIDA E COLOCA EM UMA VARIAVELL  
print(texto2)
texto2.split('\n')                                                                # SEPARA OS VALORES POR QUEBRA DE PAGINA


saldo = float(texto2.split('\n')[11].split(':')[1].replace('.','').replace(',','.')) # INSTURÇÃO PARA ALCANCAR O VALOR BUSCADO - SALDO  
print('Saldo -->',saldo)

# AUTOMATIZANDO A ANALISE DE PDF PARA VARIOS EXTRATOS

saldosmes = os.listdir()                                                          # CRIA VARIAVEL PARA RECEBER TODOS ARQUIVOS DA PASTA, NESTA PASTA FICARAO OS EXTRATOS GERAIS
saldosmes                                                                         # IMPRIME OS ARQUIVOS  

soma = 0
for saldo in saldosmes:
  relatorio3 = pdfplumber.open(saldo)
  pagina3 = relatorio3.pages[1]
  texto3 = pagina3.extract_text()
  val = float(texto3.split('\n')[15].split(':')[1].replace('.','').replace(',','.'))
  soma =soma + val
  print("Saldo:",saldo,val)
