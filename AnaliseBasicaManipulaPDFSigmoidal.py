INICIO SUBTEMA MANIUPLAÇÃO PDF
COMO PODEMOS MONTAR O DRIVE , DAI PODEMOS ACESSAR ARQUIVOS PDF
NECESSARIO INSTALAR O PDF PLUMBER
Executando o codigo de instalacao do pdfplumber
!pip install pdfplumber
O que aprendi:
Len - retorna o tamanho da variavel
Split - separando valores que tem espaçõ ou virgulas na variavel
Replace - substitui valores
Strip -remove espaçõs em branco ou caracter indesejado
Slicing - fatiar string
Step - salta nas indexações string
Capitalize - primeira letra de toda string fica maiusculo
Lower - todas letras minusculas
upper - todas letras maisuculas
title - primeira letra de cada separada vai para maisuculo
swapcase - inverte, o que era maiusculo fica minusculo e o que era minusuculo fica maiusuculo

#Executando o codigo de instalacao do pdfplumber
!pip install pdfplumber

import pdfplumber                         # IMPORTA BIBLIOTECA PARA PDF
import os                                 # IMPORTA BIBLIOTECA PARA MANIPULACAO SISTEMA OPERACIONAL        
from google.colab import drive            # IMPORTA BIBLIOTECA PARA MONTAR ACESSO AO GOOGLE DRIVE 
drive.mount('/content/gdrive')            # MONTA O ACESSO AO GOOGLE DRIVE  
pdf = pdfplumber.open('/content/gdrive/My Drive/ComPython/Curriculo Thiago F. Paoli.pdf')       # CARREGA O ARQUVIO PDF PARA A VARIAVEL PDF
pdf.pages                                 # VERIFICA AS PAGINAS DO PDF CARREGADO
pdf.pages[0]                              # ACESSA A PAGINA 1 DO PDF, LEMBRANDO QUE A INDEXACAO DE PYTHON COMEÇA COM 0
pdf.metadata                               # VERIFICA META DADOS DO PDF 

print(os.getcwd())                         # VERIFICA A PASTA QUE ESTAMOS
print(os.listdir())                        # LISTA TODOS ARQUIVOS NA PASRA QUE ESTAMOS
relatorio = pdfplumber.open('/content/gdrive/My Drive/ComPython/Curriculo Thiago F. Paoli.pdf') # CRIA OBJETO PARA RECEBER VALOR PDF
print(relatorio.pages)                     # IMPRIME O PDF 

pagina1 = relatorio.pages[0]               # CRIA UM ARQUIVO PARA COLOCAR CONTEUDO DA PG 1  
texto = pagina1.extract_text()             # EXTRAI OS DADOS DA PG 1 E COLOCA EM NOVA VARIAVEL
print(texto)                               # IMPRIME A NOVA VARAVEL COM VALORES DO PDF 1

texto.split('\n')                           # SEPARA TEXT DE ACORDO COM AS QUEBRAS DE LINHA

# SPLIT - RECORTA/SEPARA
# REPLACE TROCA UM VALOR POR OUTRO
# 
print('Nome do Candidato:',texto.split('\n')[9].split('-')[0])  # LOCALIZA NOME CANDIDATO NO PDF
print('Emaill do Candidato:',texto.split('\n')[8])              # LOCALIZA O EMAIL DO CANDIDATO NO PDF      
print("Formação do Candidato:",texto.split('\n')[39].replace('TELECOMUNICAÇÕES','TELECOM'))   # LOCALIZA FFUNCAO DO CADITADO TROCANDO PALAVRA TELECOMUNICAÇOE SPOR TELECOM
