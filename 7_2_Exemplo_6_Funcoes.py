print('\nCurso Ciência de Dados - Fundamentos em Python (Funções)\nfernandoluismc@gmail.com\n')
print('Parte 1: Criando função exemplo, imprime()\n')
print('Parte 2:Função Com Valor de Retorno\n')
print('Parte 3:Função Com Parâmetros de Intervalo, ou mais de um parâmetro\n')

#---------------------------------
#----- Parte 1 -------------------
print('----------------------------------------------\n---------- Parte 1----------------------------')

def imprime():
    print('\nExemplo 1: Esta é  uma função, sem parâmetro de entrada.\n')
imprime()

def imprime2(n):
    print('\n',n)

x = '\nImpressão desse texto inserido como parâmetro. Observe que devemos entrar com as aspas. Provavelmente tem como contornar isso para buscar de um usuário\n'
imprime2(x)

y = input('\nEscreva uma frase que gosta:  ')
imprime2(y)


#---------------------------------
#----- Parte 2 -------------------
print('----------------------------------------------\n---------- Parte 2----------------------------')

def potencia(n):
    return n*n

x = potencia(3)
print('\n',x,'\n')

#---------------------------------
#----- Parte 3 -------------------
print('----------------------------------------------\n---------- Parte 3----------------------------\n')

def intervalo(inic=1,fim=10): #Observe que existem valores padrão(Default), todavia, caso queira mudar o intervalo, basta entrar com os parâmetros início e fim
    for inic in range(1,fim+1):
        print(inic)

intervalo()
print('\n')
intervalo(1,10)
print('\n')
intervalo(3,115)
