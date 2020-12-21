print("\nEste é o programa da Maria Teresa")
x = input('\nO que vc quer fazer hj?')
print('\nA Maria Teresa disse que quer fazer:  ')
y=()
while(y!=6):
   print('Quanto é 2+2²? ')
   y = input()
   y = int(y)
   if(y==6):
      print('Acertou! Entao você pode fazer:',x)
      break
else:
   print('Errou! Vai estudar!')
