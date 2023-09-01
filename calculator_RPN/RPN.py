while True:
    stack = []
    user_str = input('Enter a numbers and operands with space: ')
    user_str = user_str.split()
    for operator in user_str:
        if operator == '+':
            x = stack.pop()
            y = stack.pop()
            stack.append(x + y)
        elif operator == '-':
            x = stack.pop()
            y = stack.pop()
            stack.append(x - y)
        elif operator == '*':
            x = stack.pop()
            y = stack.pop()
            stack.append(x * y)
        elif operator == '/':
            x = stack.pop()
            y = stack.pop()
            try:
                y == 0
            except ValueError:
                print('Is not divided into zero')
                print(f'The last of result {x}')
                stack.append(x / y)
        else:
            try:
                stack.append(int(operator))
            except ValueError:
                print('Invalid literal sign')
    try:
        print(stack[0])
    except IndexError:
        print('Invalid literal sign in list index')
    user_input = input('Do you want to exit the program? (Yes or not): ')
    if user_input.lower() == 'yes':
        exit()