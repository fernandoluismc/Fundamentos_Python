print('\nCurso Ciência de Dados - Fundamentos em Python (Listas)\nfernandoluismc@gmail.com\n')
print('Parte 1:\n')
print('Parte 2:\n')



#---------------------------------
#----- Parte 1 -------------------
print('----------------------------------------------\n---------- Parte 1----------------------------')

lst = [1,2,3,4,5]
print(lst)
lst2 = [1,2,'b',True]
print(lst2)
lst3 =[12,[1,2,3,4,5],'a',True]
print(lst3)
lst4 = list(range(0,10))
print(lst4)

print(len(lst))

print('Valor lst[3]:',lst[3])
lst[3]=3
print('Novo valor lst[3]:',lst[3])

for n in range(0,len(lst4)):
    print(lst4[n])