print('\nCurso Ciência de Dados - Fundamentos Python - List Manipulation\n Reference: Youtube - >  Python 3 Programming Tutorial -> https://www.youtube.com/watch?v=LUoKlnK5wcc\nfernandoluismc@gmail.com\n')
print('Parte 1: \n')
print('Parte 2: \n')
print('Parte 3: \n')
print('Parte 4: \n')

#---------------------------------
#----- Parte 1 -------------------
print('----------------------------------------------\n---------- Parte 1----------------------------\n')



x = [1,2,3,4,6,5,4,33,33,33,6,7,7,7,7,7] # Criando um vetor, lista qualquer

print(x) 
print('\nPrimeiro valor:',x[0],'Ultimo valor:',x[-1]) # Imprimindo valores da lista, vetor. O primeiro e o ultimo
print('\nQuantos elementos, tamanho da lista/vetor:',len(x))
print('\nPosição do primeiro elemento igual a 30 na lista;vetor:',x.index(33))
print('\nPosição do primeiro elemento igual a 30 na lista;vetor entre os valores 0 e 16:',x.index(33,0,16))
print('\nPosição do primeiro elemento igual a 30 na lista;vetor entre os valores 8 e 16:',x.index(33,8,16))
print('\nPosição do primeiro elemento igual a 30 na lista;vetor entre os valores 9 e 16:',x.index(33,9,16)) # Descobrindo a posição de valores específicos na lista,vetor. Observe que esta função
#entrega somente a posição da primeira vez q ele aparece. Como a função dá a possbilidade de indicar onde quer
# que se inicie e termine a busca, é possível ir encontrando as posições
print('\nQuantas vezes o 7 aparece, é repetido na lista,vetor:',x.count(7)) # Descobrindo quantas vezes um valor é repetido na lista,vetor


#---------------------------------
#----- Parte 2 -------------------
print('\n----------------------------------------------\n---------- Parte 2----------------------------\n')

x.append(2) # Adcionando um valor na lista/vetor, esse valor será adicionado ao final 
print(x)
print('\nQuantos elementos, tamanho da lista/vetor:',len(x))
x.insert(2,15) # Adicionando um valor na lista/vetor, esse valor será adicionado na posição indicada. OBS.: 15 na posição x[2]=3
print('\n',x)
print('\nQuantos elementos, tamanho da lista/vetor:',len(x))
x.remove(3) # Removendo um valor na lista/vetor, esse valor será adicionado na posição indicada. OBS.: posição x[2]=3
print('\n',x)
print('\nQuantos elementos, tamanho da lista/vetor:',len(x))
print('\nElemento x[3]=4º ->',x[3])
x.remove(4) # Removendo um valor na lista/vetor, esse valor será adicionado na posição indicada. OBS.: posição x[2]=2
print('\n',x)
print('\nQuantos elementos, tamanho da lista/vetor:',len(x))