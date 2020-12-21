print('\nCurso Ciência de Dados - Estatística I (Manipulação e Organização de Tabelas)\nfernandoluismc@gmail.com\n')
print('Parte 1: Importando pacotes Pandas e Numpy, onde o primeiro trata de importação de dados\nO Segundo de funções estatísticas como seleção de variáveis aleatórias simples,...\nAté o momento da aula (Set/2018) não haviam bibliotecas prontas para criação de Amostra Sistemática\nPortanto, a criação da Amostra Sistematica se dará pelo nosso desenvolvimento, e para tal\nutilizar-se-á a bibliteca math e função ceil, onde math é uma biblioteca nativa do python\n')
print('Parte 2: Importando Conjunto de Dados do tipo csv, utilizando a biblioteca pandas\nChecando quantos valores de cada tipo, possuem em uma coluna utilizando a função dB_name[','classe','].value_counts()\n')
print('Parte 3: Exemplo Youtube: Importação de arquivos, busca e filtragem de dados em dataframes,... https://www.youtube.com/watch?v=e60ItwlZTKM \n')
print('Parte 4: \n')
#---------------------------------
#----- Parte 1 -------------------

print('----------------------------------------------\n---------- Parte 1----------------------------\n')

import pandas as pd
print('\nA versão do pandas é: ',pd.__version__)
import numpy as np 
print('A versão do numpy é:',np.__version__)
import scipy as stats
print('A versão do scipy é:',stats.__version__)
import statistics as stat

#---------------------------------
#----- Parte 2 -------------------
print('----------------------------------------------\n---------- Parte 2----------------------------\n')

jogadores = pd.read_csv("/home/fernandoluismc/Documents/Curso_Cien_Dados/Estatistica_I/Dados/jogadores.csv") #Importando conjunto de dados
print(jogadores,'\n') #Checando valores dos conjuntos de dados
print(type(jogadores)) #Checando tipo do conjunto de dados


jogadores.columns = ['Jogador','Salário'] #Colocando nome nas colunas dos dados
jogadores.rows = ['Felipe Luis','Rodrigo Caio','Arão','Everton Ribeiro','Arrascaeta','Bruno Henrique','Diego Ribas','Gabigol']
print('\n',jogadores.columns)
print('\n',jogadores.rows)
print('\n\n',jogadores)
#jogadores = pd.to_excel("/home/fernandoluismc/Documents/Curso_Cien_Dados/Estatistica_I/Dados/jogadores.xls")

#print(df[df['Jogador']=='1'])




#---------------------------------
#----- Parte 3 -------------------


print('----------------------------------------------\n---------- Parte 3----------------------------\n')

print('\n O tutorial pode ser acessado em https://www.youtube.com/watch?v=e60ItwlZTKM , último acesso 21/01/2010\n') 

print('[2] Baixando/Carregando arquivo')
fremont_weather = pd.read_csv('/home/fernandoluismc/Documents/Curso_Cien_Dados/Fundamentos_Python/Pandas_Introduction/Fremont_weather.txt')
print('\n\n')

print(fremont_weather,'\n')



##### Imprimindo as 5 primeiras linhas ou as últimas 3 linhas #####
print('\n[3.1]Imprimindo as 3 últimas linhas\n',fremont_weather.tail(3),'\n') #Observe a notação tail

print('\n[3.2]Imprimindo as 5 primeiras linhas\n',fremont_weather.head(5),'\n') #Observe a notação para as 5 primeiras linhas

print('\n[3.3]Imprimindo as 5 primeiras linhas com a notação df.[linha_inic:linha_fin]\n',fremont_weather[0:5],'\n') #Observe a notação para as 5 primeiras linhas e atenção, pois
#inicia-se em 0

##### Buscando Valores em Conjunto de Dados #####

print('\n[4.1] Tipos dos objetos contidos no conjunto de dados:\n',fremont_weather.dtypes,'\n')
print('\n[4.2] Indexadores do conjunto de dados:\n',fremont_weather.index,'\n')
print('\n[4.3] Colunas do conjunto de dados:\n',fremont_weather.columns,'\n')
print('\n[4.4] Valores do conjunto de dados:\n',fremont_weather.values,'\n')

########### Resumo Estatístico do Conjunto de Dados ###########
print('\n[5]\n',fremont_weather.describe(),'\n') #Resumo Estatístico

########### Apresentação de Dados por meio de sorteio de algum dos valores ###########

print('\n[6] Buscando valores sorteados pela coluna Record High\n',fremont_weather.sort_values('record_high',ascending=False)) 

########### Seleção, Busca, Divisão de Valores Específicos ###########

print('\n[7.1.1] Buscando valores da coluna Average Low\n',fremont_weather.avg_low)
print('\n[2.1] Buscando valores da coluna Average Low\n',fremont_weather['avg_low'])

print('\n[7.2] Buscando valores de linhas específicas\n',fremont_weather[2:4])  #Observe que não se busca o dado da última linha

print('\n[7.3.1] Buscando todos os valores de colunas específicas\n',fremont_weather[['avg_low','avg_high']]) #Observe que utiliza-se duas chaves!!!


print('\n[7.3.2] Buscando todos os valores de Colunas específicas\n',fremont_weather.loc[:,['avg_low','avg_high']]) #Observe que utiliza-se duas chaves!!!
#                                                                 df.loc[from_row:to_row,['column1','column2']]

print('\n[7.4] Buscando valores de linhas e colunas específicas\n\n',fremont_weather.loc[9,['avg_precipitation']],'\n')

print('\n[7.5.1] Buscando valores múltiplos de linhas e colunas específicas\n\n',fremont_weather.iloc[3:5,[0,3]],'\n')
# .iloc = index location
print('\n[7.5.2] Buscando valores múltiplos de linhas e colunas específicas\n\n',fremont_weather.iloc[3:5,[0,1,3]],'\n')

print('\n[7.5.3] Buscando valores múltiplos de linhas e colunas específicas\n\n',fremont_weather.iloc[3:5,[0]],'\n')

### Observe que para buscar valores em com indexadores de linhas e colunas, não se utiliza o nome da coluna em questão 

#print('\nBuscando valores múltiplos de linhas e colunas específicas\n\n',fremont_weather.iloc[3:5,['avg_high']],'\n')

#print('\nBuscando valores múltiplos de linhas e colunas específicas\n\n',fremont_weather.iloc[3:5,['month','avg_high','record_high']],'\n') 

########### Filtragem de Valores de um Conjunto de Dados ###########


print('\n[8.1] Filtrando valores de Colunas\n\n',fremont_weather[fremont_weather.avg_precipitation > 1.0],'\n')

print('\n[8.2] Filtrando dados de um dado já filtrado, exemplo: em relação aos meses somente alguns meses\n\n',fremont_weather[fremont_weather['month'].isin(['Jun','Jul','Aug'])])

###########   Substituindo ou atribuindo valores - Assignment - very similar to slicing ###########

fremont_weather.loc[9,['avg_precipitation']] = 101.3
print('\n[9.1] Valor 101.3 substituído em fremont_weather.iloc[9,[\'avg_precipitation\']\n',fremont_weather.iloc[9:11])

fremont_weather.loc[9,['avg_precipitation']] = np.nan
print('\n[9.2] Valor NaN substituído em fremont_weather.iloc[9,[\'avg_precipitation\']\n',fremont_weather.iloc[9:11])
#Observe q np.nan é uma valor vindo de numpy


fremont_weather.loc[:,'avg_low'] = np.array([5]*len(fremont_weather)) 
print('\n[9.3] Substituindo valor em todas as linhas de uma coluna. Utilizando fremont_weather.loc[:,\'avg_low\']\n',fremont_weather.head())


fremont_weather['avg_day'] = (fremont_weather.avg_low + fremont_weather.avg_high)/2
print('\n[9.4] Somando os valores de avg_low e avg_high e dividindo por 2 (Média) adicionando a uma coluna extra. Utilizando fremont_weather.loc[:,\'avg_low\']\n',fremont_weather.head())


###########   Renomeando Colunas ###########

fremont_weather.rename(columns = {'avg_precipitation':'avg_rain'},inplace=True) #Renomeando coluna 1
print('\n[10] Renomeando somente 1 Coluna \n',fremont_weather.head())

fremont_weather.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print('\n[10] Renomeando todas as Colunas \n',fremont_weather.head())

###########   Iteração com dataframe ###########

print('\n',fremont_weather,'\n')

for index, row in fremont_weather.iterrows():
    print(index,row["month"], row["av_hi"])

print('\n',fremont_weather,'\n')

###########   Salvando arquivo csv ###########

fremont_weather.to_csv('/home/fernandoluismc/Documents/Curso_Cien_Dados/Fundamentos_Python/Pandas_Introduction/Fremont_weather')

###########   Algumas operações ###########

# Somando valores em uma coluna
teste =[1,2,3,4]
print(teste)
tteste = np.transpose(teste)
print('\n\nTeste: ',tteste)
fremont_weather.columns = ['month','avg_high','avg_low','record_high','record_low','avg_rain','av_day']
fremont_weather['avg_day'] = (fremont_weather.avg_high + stat.mean(fremont_weather.avg_low) + stat.stdev(fremont_weather.avg_high))
print('\n',fremont_weather,'\n')
#transposed = fremont_weather.avg_high.T()
print('\nAvg_high: ',fremont_weather.avg_high,'\n\nMédia Avg_low: ',stat.mean(fremont_weather.avg_low),'\n\nDesvio Padrão Avg High: ',stat.stdev(fremont_weather.avg_high))
