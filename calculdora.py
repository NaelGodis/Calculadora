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
number_2 = int(input('Enter your  number:'))

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

#o usuário deverá realizar novo cálcullo sem executar a aplicação novamente
def calculate():
    operation = input('''
    Please type in the mach operation you wold like to complte:
    + for addition
- for subtraction
* for multiplication
/ for division
    ''')



#Add again() function to calculate() function
    again()
def again():
    calc_again = input('''
    Do you want to calculate again?
    please type Y for YES or N for NO.
    ''' )

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Se you later.')
    else:
        again()

calculate()