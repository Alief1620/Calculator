import sys

stack = []
OPERATORS = ['+', '-', '*', '/']
YES = 'yes'


def calculate(argument_1: int, argument_2: int, operator: str) -> int:
    match operator:
        case '+':
            return argument_2 + argument_1
        case '-':
            return argument_2 - argument_1
        case '*':
            return argument_2 * argument_1
        case '/':
            try:
                argument_1 / argument_2
            except ZeroDivisionError:
                print('Division by zero is not allowed')
                print(f'The last result: {argument_1}')
            return argument_2


def number_of_elements(stack: int) -> int:
    return len(stack) < 2


def user_string_calculator_formatter(user_str: str) -> int:
    for element in user_str:
        if element.isdigit():
            stack.append(int(element))
        elif element in OPERATORS:
            if number_of_elements(stack):
                print('Not enough operands for')
                break
            stack.append(calculate(stack.pop(0), stack.pop(0), element))
        else:
            print('Invalid input:', element)
            break
    try:
        print(stack[0])
    except IndexError:
        print('Invalid literal sign in list index')


def clear_user_stack() -> bool:
    user_response = input('Do a calculation with the past result? (Yes or No): ')
    return user_response != YES


def want_to_continue() -> bool:
    user_response = input('Do you want continue? (Yes or No):')
    return user_response != YES


def run() -> None:
    while True:
        user_str = input('Enter a numbers and operators separated by spaces: ')
        user_str = user_str.split()
        user_string_calculator_formatter(user_str)
        if clear_user_stack():
            stack.clear()
            if want_to_continue():
                sys.exit()


run()
