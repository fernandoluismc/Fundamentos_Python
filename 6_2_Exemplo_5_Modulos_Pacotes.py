print('\nCurso Ciência de Dados - Fundamentos em Python (Modulos e Pacotes)\nfernandoluismc@gmail.com\n')
print('Parte 1:\n')
print('Parte 2:\n')


#---------------------------------
#----- Parte 1 -------------------
print('----------------------------------------------\n---------- Parte 1----------------------------')

import statistics as est
import math
from statistics import mean,median
from statistics import*
z = [10,20,20,40]
x = est.mean(z)
y = est.median(z)
x1 = mean(z)
y1 = median(z)
dp1 = stdev(z)
print('\nConjunto de dados criado: ',z)
print('\nMédia: ',x)
print('\nMediana: ',y)
print('\nMédia: ',x1)
print('\nMediana: ',y1)
print('\nDesvio Padrão Calculado pela função statistics.stdev: ',dp1,'  Observe que há diferença do desvio padrão calculado, provavelmente pq a função utiliza algum espaço amostra dessa lista que é pequena\n') 
z1 = [zi-mean(z) for zi in z]
print('\nDiferença entre elementos e média da lista: ',z1,'\n')
z_square= [pow(z1i,2) for z1i in z1]
print('\nQuadrado da diferença calculada acima: ',z_square,'\n')
z_total = sum(z_square)
print(z_total/len(z))
print("\nO desvio padrão é:", math.sqrt(z_total/len(z)),'\n')
