print('\nCurso Ciência de Dados - Fundamentos em Python (Objetos e Tipos de Variáveis)\nfernandoluismc@gmail.com\n')
print('Parte 1:Tipos de Variáveis e Transformação de Variáveis \n')
print('Parte 2:Operadores Matemáticos e Entrada de dados\n')

#--------------------------------
#------Variáveis-----------------
x = 1
y =3.13
m ="python1"
n='python2'
w = True
Y = False

#---------------------------------
#----- Parte 1 -------------------
print('----------------------------------------------\n---------- Parte 1----------------------------')
print('\nEsta é a variável',y, 'do tipo',type(y))

print('\nTemos portanto alguns tipos de variáveis,sendo\n',x,':',type(x),'\n',y,":",type(y),'\n',m,':',type(m),'\n',n,':',type(n),'\n',w,':',type(w),'e\n',Y,':',type(Y))

x = int(x)
y=float(y)

print('\nApós a transformação de variáveis, tem-se:\nx = int(x)   -->',type(x),
'\ny = float(y) -->',type(y))
#---------------------------------
#----- Parte 2 -------------------
print('----------------------------------------------\n---------- Parte 2----------------------------')
print('O programa irá realizar o seguinte cálculo: (x+y)*y²')
x = input('Insira o valor de x: ')
x = float(x)
s = input('Insira o valor de y: ')
s = float(s)
resultado = (x+s)*(pow(s,2)) #Observação: potencia utilizando ** está dando errado
print('O resultado é:',resultado)

