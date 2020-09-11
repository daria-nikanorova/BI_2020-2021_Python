while True:
    #Try and except allow us to find ValueError if user enters characters instead of numbers
    try:
        first_operand = float(input("Enter first number "))
    except ValueError:
        print('Input value is not a number! Please, try again: ')
        continue
    operator = input('Enter an operation: + for addition, - for substraction, / for division, * for multiplication, '
                     '// for floor division, % for modulus, ** for exponent ')
    #Next part prevents from using other operands
    if operator not in ['+','/','//','%', '-', '*', '**']:
        print('Please choose an operand from the list below!')
        operator = input('Enter an operation: + for addition, - for substraction, / for division, * for multiplication, '
                     '// for floor division, % for modulus, ** for exponent ')
    #Again try and except allow us to find ValueError if user enters characters instead of numbers
    try:
        second_operand = float(input("Enter second number "))
    except ValueError:
        print('Input value is not a number! Please, try again: ')
        continue
    #This part prohibit dividing by zero
    if (operator in ['/','//','%']) and (second_operand == 0):
        second_operand = float(input("You can`t divide by zero! Please enter another second number "))
        if second_operand == 0:
            print('Please try again and don`t DIVIDE BY ZERO!')
            continue
    if operator == '+':
        result = first_operand + second_operand
        print(result)
    if operator == '-':
        result = first_operand - second_operand
        print(result)
    if operator == '/':
        result = first_operand / second_operand
        print(result)
    if operator == '*':
        result = first_operand * second_operand
        print(result)
    if operator == '//':
        result = first_operand // second_operand
        print(result)
    if operator == '%':
        result = first_operand % second_operand
        print(result)
    if operator == '**':
        result = first_operand ** second_operand
        print(result)
    continue_or_exit = input('Do you want to continue? Yes/No ')
    if continue_or_exit == "No":
        print('Bye!')
        break
