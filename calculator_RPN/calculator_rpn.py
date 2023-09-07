import sys

stack = []
OPERATORS = ['+', '-', '*', '/']
YES = 'yes'


def get_user_input():
    user_str = input('Enter a numbers and operators separated by spaces: ')
    return user_str.split()


def calculate(argument_1, argument_2, operator):
    match operator:
        case '+':
            return argument_2 + argument_1
        case '-':
            return argument_2 - argument_1
        case '*':
            return argument_2 * argument_1
        case '/':
            try:
                return argument_2 / argument_1
            except ZeroDivisionError:
                print('Division by zero is not allowed')
                print(f'The last result: {argument_2}')
            return argument_2


def user_string_calculator_formatter(user_str):
    for element in user_str:
        if element.isdigit():
            stack.append(int(element))
        elif element in OPERATORS:
            try:
                len(stack) < 2
            except ValueError:
                print('Not enough operands for')
            stack.append(calculate(stack.pop(), stack.pop(), element))
        else:
            print('Invalid input:', element)
            break
    try:
        print(stack[0])
    except IndexError:
        print('Invalid literal sign in list index')

    user_response = input('Do a calculation with the past result? (Yes or No): ')
    if user_response != YES:
        stack.clear()

    user_response = input('Do you want to continue? (Yes or No): ')
    if user_response != YES:
        sys.exit()


def run():
    while True:
        user_string_calculator_formatter(get_user_input())


run()
