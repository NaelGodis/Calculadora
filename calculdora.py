#adiçao
number_1 = int(input('Entre com o primeiro número'))
number_2 = int(input('Entre com o segundo número'))
print ('{} + {} = ' .format(number_1,number_2))
print(number_1 + number_2)


#subtração
print ('{} - {} = ' .format(number_1,number_2))
print(number_1 - number_2)

#multiplicação
print ('{} * {} = ' .format(number_1,number_2))
print(number_1 * number_2)

#divisão
print ('{} / {} = ' .format(number_1,number_2))
print(number_1 / number_2)

#permitir que o usuário  selecione a operação que deseja
operation = input('''Please type in the mach operation you wold like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

number_1 = int(input('Enter your first number:'))
number_2 = int(input('Enter your first number:'))

if operation == '+':
    print ('{} + {} =' .format(number_1,number_2))
    print(number_1 + number_2)

elif operation == '-':
    print ('{} - {} =' .format(number_1,number_2))
    print(number_1 - number_2)

elif operation == '*':
    print ('{} * {} =' .format(number_1,number_2))
    print(number_1 * number_2)

elif operation == '/':
    print ('{} / {} =' .format(number_1,number_2))
    print(number_1 / number_2)

else:
    print('You have not typed a valid operator, please run the programm again.')