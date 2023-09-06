stack = []
OPERATORS = ['+', '-', '*', '/']
YES = 'yes'


def get_user_input():
    user_str = input('Enter a numbers and operators separated by spaces: ')
    return user_str.split()


def calculate(x, y, operator):
    match operator:
        case '+':
            return y + x
        case '-':
            return y - x
        case '*':
            return y * x
        case '/':
            if x == 0:
                print('Division by zero is not allowed')
                print(f'The first operand: {y}')
                return y
            return y / x


def user_string_calculator_formatter(user_str):
    for element in user_str:
        if element.isdigit():
            stack.append(int(element))
        elif element in OPERATORS:
            if len(stack) < 2:
                print('Not enough operands for')
                break
            stack.append(calculate(stack.pop(), stack.pop(), element))
        else:
            print('Invalid input:', element)
            break
    try:
        print(stack[0])
    except IndexError:
        print('Invalid literal sign in list index')


def has_to_clear_user_stack():
    user_response = input('Do you want to make a calculation with the previous result? (Yes or No): ')
    return user_response != YES


def has_to_continue():
    user_response = input('Do you want to continue? (Yes or No): ')
    return user_response != YES


def run():
    while True:
        user_string_calculator_formatter(get_user_input())
        if has_to_clear_user_stack():
            stack.clear()
            if has_to_continue():
                exit()


run()

