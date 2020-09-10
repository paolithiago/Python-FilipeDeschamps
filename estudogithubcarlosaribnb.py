# -*- coding: utf-8 -*-
"""EstudoGithubCarlosAribnb.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qcS_nfQl3FELrQLBTO-6ktn4OMgyL0BG
"""



"""Este estudo visa verificar sobre o estudo de caso do Carlos Sigmoidal sobre Airbnb. De acordo com o estudo de caso oo dataset esta no link abaixo:

http://data.insideairbnb.com/brazil/rj/rio-de-janeiro/2019-07-15/visualisations/listings.csv

O Airbnb já é considerado como sendo a maior empresa hoteleira da atualidade. Ah, o detalhe é que ele não possui nenhum hotel!

Conectando pessoas que querem viajar (e se hospedar) com anfitriões que querem alugar seus imóveis de maneira prática, o Airbnb fornece uma plataforma inovadora para tornar essa hospedagem alternativa.

Uma das iniciativas do Airbnb é disponibilizar dados do site, para algumas das principais cidades do mundo. Por meio do portal Inside Airbnb, é possível baixar uma grande quantidade de dados para desenvolver projetos e soluções de Data Science.

Neste notebook, iremos analisar os dados referentes à cidade do Rio de Janeiro, e ver quais insights podem ser extraídos a partir de dados brutos.

http://insideairbnb.com/get-the-data.html 
acima o site com Os dados por trás do site Inside Airbnb são obtidos de informações disponíveis publicamente no site do Airbnb.
"""

#Para esta analise vamos utilizar o o arquivo listings.csv - Summary information and metrics for listings in Rio de Janeiro (good for visualisations).

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd #O pandas é uma ferramenta de análise e manipulação de dados de código aberto rápida, poderosa, flexível e fácil de usar,
import matplotlib.pyplot as plt #Matplotlib é uma biblioteca abrangente para a criação de visualizações estáticas, animadas e interativas em Python.
import seaborn as sns#Seaborn é uma biblioteca de visualização de dados Python baseada em matplotlib . Ele fornece uma interface de alto nível para desenhar gráficos estatísticos atraentes e informativos.
# %matplotlib inline

df = pd.read_csv("/content/listings.csv")#Carrgea  arquivo csv

df.head(3)#consegue avaliar as tres primeiras linhas

"""Análise dos Dados
Esta etapa tem por objetivo criar uma consciência situacional inicial e permitir um entendimento de como os dados estão estruturados.

Dicionário das variáveis



1.   id - número de id gerado para identificar o imóveln
1.   name - nome da propriedade anunciada
2.   host_id - número de id do proprietário (anfitrião) da propriedade
1.   host_name - Nome do anfitrião
1.  neighbourhood_group - esta coluna não contém nenhum valor válido
1.  neighbourhood - nome do bairro
1.   latitude - coordenada da latitude da propriedade
1.  longitude - coordenada da longitude da propriedade
2.  room_type - informa o tipo de quarto que é oferecido
2.   price - preço para alugar o imóvel
2.   minimum_nights - quantidade mínima de noites para reservar
2.   number_of_reviews - número de reviews que a propriedade possui
2.   last_review - data do último review
1.   reviews_per_month - quantidade de reviews por mês
2.   calculated_host_listings_count - quantidade de imóveis do mesmo anfitriã
1.   availability_365 - número de dias de disponibilidade dentro de 365 dias

Antes de iniciar qualquer análise, vamos verificar a cara do nosso dataset, analisando as 5 primeiras entradas.
"""

#Shape - shape Retorne uma tupla representando a dimensionalidade do DataFrame.
print("Variavies: \t {}".format(df.shape[0]))#faz contagem na dmensao linhas
print("Dados: \t {}".format(df.shape[1]))#faz contagem na fimensao colunas
#nosso dataset tem 35451 linhas e 16 colunas

display(df.dtypes)#verifica e imprime a caoluna e seu tipo

"""Q2. Qual a porcentagem de valores ausentes no dataset?
A qualidade de um dataset está diretamente relacionada à quantidade de valores ausentes. É importante entender logo no início se esses valores nulos são significativos comparados ao total de entradas.

É possível ver que a coluna neighbourhood_group possui 100% dos seus valores faltantes.
As variáveis reviews_per_month e last_review possuem valores nulos em quase metade das linhas.
As variáveis name e host_name têm aproximadamente 0,1% dos valores nulos.

ABAIXP VAMOS VERIFICAR POR COLUNA A SITUACAO DE VALORES NULOS
"""

print(df.isnull().sum())# Comando que verifica quantos valores nulos tem nas linhas por colunas
print("\n")
(df.isnull().sum()/df.shape[0]).sort_values(ascending = False)#faz um  de linhas nulas e ordena

"""Q3. Qual o tipo de distribuição das variáveis?
Para identificar a distribuição das variáveis, irei plotar o histograma.
"""

#imprime histograma com todos as colunas
df.hist(bins=15 , figsize=(20,15))



"""Conforme os graficos acima, e possivel verificar se temos utliers nas distribuicoes? Sim, por exemplo por exemplo calculated_host_listings_count. Para isso podemos usar o describe que nos traz informações sobre dados estatisticos"""

#Describe faz as analises estatisticas de todas colunas, porem podems setar qual coluna queremos verificar
df.describe()

df[['price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month',
    'calculated_host_listings_count', 'availability_365']].describe()

# oque podemos ver e que em price 75% dos dados estao abaixo de 599 porem o valor maximo e 4000(precisaria analisar este outlier)



"""Veja a diferença entre os comandos, no caso do describe sem especificar as colunas e especificando as colunas.
Quando precisa usar colunas colocar o df e as colunas dentro de colchetes
"""



"""Agora vamos fazer um plot para que possamos verificar valores acima de 20 dias na variavel minimum_nights que e quantidade de dias minimmos de noites para reservar"""

#primeiro vamos Analisar a coluna -  Assim temos 35451 valores do tipo int com o menor valor sendo 1 e o maior sendo 1123 noites para reservar, 
# o que pode ser de fato outlier
print(df['minimum_nights'])
print("Valor Maximo",df['minimum_nights'].max())
print("Media de valores",df['minimum_nights'].mean())
print("Valor Minimo",df['minimum_nights'].min())
print("Desvio Padrao",df['minimum_nights'].std())

df['minimum_nights'].plot(kind = 'box', vert = False, figsize=(15,8))#Criei uma visao em que analiso a colna minimun nights plotando um grafico
#do tipo bos na horizontal com tamanho 15,8
nightMaior20 = len(df[df.minimum_nights>30])#coloquei em uma variavel a analise de casos maiores que 30 na coluna
print("Valores acima de 30 dias -->",nightMaior20)#imprimo a quantidade de valores acima de 30
print("Repreentacao -->{:.2f}%".format((nightMaior20/df.shape[0])*100))#imrpimo o %  acima de 30 sobre todos os valores

#Agora vamos criar o mesmo grafico de cima agora para coluna Price
print("Valores",df.price) #aqui imprimos todos valores da coluna
print("Valor Maximo: {:.2f}".format(df.price.max()))
print("Media: {:.2f}".format(df.price.mean()))#aqui imprimimos a media dos valores da coluna price
print("Valor Minimo: {:.2f}".format(df.price.min()))#Aqui imprimimos o valor minimo
print("Valor Desvio Padrao: {:.2f}".format(df.price.std()))
#Pela Analise temos valores de 0 ate 40000

#Agora vamos plotar os valors em graficos
df.price.plot(kind = 'box', vert = False , figsize = (15,6))
plt.show()

# ver quantidade de valores acima de 1500 para price
valpriceMaior1500 = len(df[df.price>1500])
print("Valores Acima de 1500: {:.2f}".format(valpriceMaior1500))
print("Representacao sobre todo:{:.2f}%".format((valpriceMaior1500/df.shape[0])*100))

#agora imprimri novamente os Histogramas sem outliers #PRECISO ESTUDAR AQUI
# remover os *outliers* em um novo DataFrame
df_clean = df.copy()#cria uma varavel que copia
df_clean.drop(df_clean[df_clean.price > 1500].index, axis=0, inplace=True)#usa drop para colocar somrne valores sem outlier 1500
df_clean.drop(df_clean[df_clean.minimum_nights > 30].index, axis=0, inplace=True)#usa drop para colocar somrne valores sem outlier maiores que 30

# remover `neighbourhood_group`, pois está vazio
df_clean.drop('neighbourhood_group', axis=1, inplace=True)

# plotar o histograma para as variáveis numéricas
df_clean.hist(bins=15, figsize=(15,10));

"""Q4. Qual a correlação existente entre as variáveis
Correlação significa que existe uma relação entre duas coisas. No nosso contexto, estamos buscando relação ou semelhança entre duas variáveis.

Essa relação pode ser medida, e é função do coeficiente de correlação estabelecer qual a intensidade dela. Para identificar as correlações existentes entre as variáveis de interesse, vou:

Criar uma matriz de correlação
Gerar um heatmap a partir dessa matriz, usando a biblioteca seaborn
"""

#Crar uma matriz de correlação. Aqui com  FUNCAO CORR faz uma correlacao entrea as coluna inclusive com ela mesma
corr = df_clean[['price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month',
    'calculated_host_listings_count', 'availability_365']].corr()
display(corr)

#Agora criar um mapa de calor com os dados acima
sns.heatmap(corr,cmap='RdBu', fmt = '.2f', square = True,linecolor='white', annot=True)

"""Q5. Qual o tipo de imóvel mais alugado no Airbnb?
A coluna da variável room_type indica o tipo de locação que está anunciada no Airbnb. Se você já alugou no site, sabe que existem opções de apartamentos/casas inteiras, apenas o aluguel de um quarto ou mesmo dividir o quarto com outras pessoas.

Vamos contar a quantidade de ocorrências de cada tipo de aluguel, usando o método value_counts().italicized text

**values_counts conta ocorrencia por tipo da coluna**
"""

# Mostra a quantidade de valores/ocorrencias por tipo da coluna exe, home apt primvate room etc
print(df_clean.room_type.value_counts())

#agora vaos usar formula shape[0] para fazer o percentual por tipo da coluna room type
tipos_roomtype = df_clean.room_type.value_counts() #aqui coloquei em uma variavel a contagem de valores por ocorrencias
(tipos_roomtype/df_clean.shape[0]*100)# aqui faco o calculo da variavel contada pelo total de count dividido por 100 para ter %

"""Q6. Qual a localidade mais cara do Rio?
Uma maneira de se verificar uma variável em função da outra é usando groupby(). No caso, queremos comparar os bairros (neighbourhoods) a partir do preço de locação.
"""

#aqui  criamos um comando que usa a variavel para df_clean agrupando atraves do group by pela coluna neighbourhood, pela media de preco usando sort.values para ser
#ordenanda do maior para o menor e [:10] traz os dez primeiros valores
df_clean.groupby(['neighbourhood']).price.mean().sort_values(ascending=False)[:10]



"""Agora vamos ver quantos emprrendimentos estao no complexo do alemao contando e imprimindo"""

# ver quantidade de imóveis no Complexo do Alemão
print(df[df.neighbourhood == "Complexo do Alemão"].shape)# aqui usamos especificamente analise da coluna neigh se e igual a complexo do alemao e com shape ve linhas  e colunas
df[df.neighbourhood == "Complexo do Alemão"]

# plotar os imóveis pela latitude-longitude
#no grafico abaixo imprime valor de lonigtude em x , latitude em y 
df_clean.plot(kind="scatter", x='longitude', y='latitude', alpha=0.4, c=df_clean['price'], s=8,
              cmap=plt.get_cmap('jet'), figsize=(12,8));
