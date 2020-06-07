#!/usr/bin/env python
# coding: utf-8

# In[ ]:





#  Aqui nesta aula o professor ensia a acessar dois arquivos usando modulo panda. Scessar os raw de dois aruqivos de filems usando panda  e read.
#  Video - Data Science: Introdução a Ciência de Dados (Primeira aula prática programando em Python 
#  - Assiti no dia 07/06/20
# https://www.youtube.com/watch?v=F608hzn_ygo
# 

# In[13]:


import pandas as pd #importa dados do modulo panda
uri ="https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv" #salva http onde o arquvio esta 
filmes = pd.read_csv(uri)#joga a leitura de todas as linhas do arquivo para a variavel filmes
filmes.columns=['idfilme','titulos','genero']#renomeia os titulos das colunas
filmes.head()#abre as 5 primeiras linhas


# In[4]:


uri2 ="https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"#carrega os dados do http
notas = pd.read_csv(uri2)#atribui a tabela csv a variavel notas
notas.columns = ['idusuario','idfilme','nota','momento']#renomia as colunas
notas.head()#imprime as 5 lihas


# In[5]:


notas["nota"]#retorna a coluna nota da variavel nota que recebeu a tabela


# In[6]:


notas["nota"].head()#retorna a coluna nota da variavel nota que recebeu a tabela porem as primeiras linhas


# In[7]:


notas["nota"].unique()#retorna os valores que sao unicos das notas da variavel nota que recebeu va variavel


# In[8]:


notas["nota"].mean()#retorna a media das notas na coluna nota da variavel notas que recebe o csv com as notas dos filmes


# In[9]:


notas["nota"].max()#retorna  valor maximo dos valores de nota o min e median e so alterar


# In[10]:


notas.describe()#descreve todas as medidas pore coluna


# In[14]:


notas["nota"].median()


# Video MELHOR FORMA DE APRENDER PYTHON (Google Colab Notebook) - Assisti no dia 07/06/20
# https://www.youtube.com/watch?v=Gojqw9BQ5qY
# 

# In[15]:


nome = 'carlos'
print(nome)


# In[16]:


idade = 39


# In[17]:


idade


# In[18]:


idade +=2


# In[19]:


print(idade)


# In[21]:


print(idade)


# In[24]:


#funcao que recebe idade e soma com mais um
def idade (i):
    i = i+1
    return i
idade(1000)
    


# In[25]:


#exemplo de listas com funcoes. Varios filmes
filme1 = 'galo'
filme2='matrix'
filme3 = 'jonh'


# In[26]:


#estrutura para armazenar valor, ao inves de fazer conforme acima com um monte de variaveis, pode jogar os valores em uma lista
#entre coclhetes
filmes = ['galo','matrix','jonh']#joga as strings para a lista
print(filmes)#imprime valores


# In[29]:


#agora imprimir uma funcao para receber a lista de filmes, e colocar um texto ante informando que é a lista que quer imprimr
def listaFilmes(filmes_imprimir):#cria a fucao com nome listafilmes que recebe um argumento chamado filmes_imprimir. 
    print("Filmes que quero impimir")#imprime um texto padrao
    print(filmes_imprimir)#imprime a lista que recebeu de fonte externa usada o argumento filmes_imprimir


# In[30]:


listaFilmes(filmes)


# In[35]:


# so que no caso ou queria mostrar um embaixo do outro  ou imprimindo indexado. Veja abaixo gostaria de imprir assim:

filmes[0]


# In[36]:


filmes[1]


# In[37]:


filmes[2]


# In[38]:


#posso usar um loop for com o tamnho da lista e a variavel do loop recebe lista e depois imprime
for i in filmes:
    print(i)


# In[39]:


#indexações na lisa -1 e o ultimo valor
filmes[-1]


# In[40]:


#indexações na lisa 0 é o primeiro, e assim vai
filmes[0]


# In[42]:


#indexações na lista index mais : siginifca que a partir do indice para frente
filmes[1:]


# In[48]:


#criada a funcao que recebe uma valor de lista de filmes, pelo nome listaFilmes, com argumento de entrada filmes_imprimir,
#depois impime um texto padrão, e gera um fr do tamnha da lista com o argumento recebido de entrada , e depois imprime os filmes
#dai tem a chamada da função
def listaFilmes(filmes_imprimir). 
    print("Lista que quero impimir")
    for i in filmes_imprimir:
        print(i)
listaFilmes(filmes)


# In[62]:


#criando um dicionario com nome do paoli e a idade
dadosPaoli={
        "nome":"thiago","idade":37,
        "empresa":"oi"
      }


# In[64]:


dadosPaoli


# In[61]:


dados["nome"]


# In[ ]:




