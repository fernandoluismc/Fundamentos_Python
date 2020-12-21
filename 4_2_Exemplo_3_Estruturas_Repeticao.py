print('\nCurso Ciência de Dados - Fundamentos em Python (Estruturas de Repetição)\nfernandoluismc@gmail.com\n')
print('Parte 1: Utilização função while\n')
print('Parte 2: Utilização função for\n')



#---------------------------------
#----- Parte 1 -------------------
print('----------------------------------------------\n---------- Parte 1----------------------------')

count = 1
while count <= 5:
    print(count)
    count +=1

#---------------------------------
#----- Parte 2 -------------------
print('----------------------------------------------\n---------- Parte 2----------------------------')

for n in range(0,10,1):
    print(n+1)

print('\n')
for n2 in range(10,0,-1): # Contagem Regressiva
    print(n2)
print('\n')
for n3 in range(0,10,1):
    if n3==4:
        break # Aborta o laço
    print(n3)

    print('\n')
for n4 in range(0,10,1):
    if n4==4:
        continue # Pula o laço, porém continua
    print(n4)