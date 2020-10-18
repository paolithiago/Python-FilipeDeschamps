#biblioteca qie carrega arquivos no google drive
from google.colab import drive

#Monta o drive - para isso precisa digitar abaixo e clicar no link, fazer o acesso no google drive e copiar o link informado
drive.mount('/content/gdrive')

!ls 'gdrive/My Drive/ComPython'                # LISTA ARQUVIVOS DE UMA PASTA - FAZER SIMILAR AO DOS


#*************************** MONTANDO DIRETORIO GMAIL E ACESSANDO ARQUIVOS, PASTAS********************************
os.getcwd()                                    # VERIFICA QUAL DIRETORIO ESTAMOS NO DRIVE
os.chdir('/content/gdrive/My Drive/ComPython') # ALTERA A PASTA PARA UMA QUE VOCE DESEJA
os.getcwd()                                    # CONSULTA NOVAMENTE A PASTA ATUAL
os.listdir()                                   # LISTA ARQUIVOS DENTRO DO DIRETORIO ATUAL

