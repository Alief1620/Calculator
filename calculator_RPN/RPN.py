while True:
    stack = []
    user_str = input('Enter a numbers and operands with space: ')
    user_str = user_str.split()
    for operator in user_str:
        if operator == '+':
            x = stack.pop(0)
            y = stack.pop(0)
            stack.append(x + y)
        elif operator == '-':
            x = stack.pop(0)
            y = stack.pop(0)
            stack.append(x - y)
        elif operator == '*':
            x = stack.pop(0)
            y = stack.pop(0)
            stack.append(x * y)
        elif operator == '/':
            x = stack.pop(0)
            y = stack.pop(0)
            if y == 0:
                print('Division by zero is not allowed')
                print(f'The last result: {x}')
                break
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
    user_input = input('Do you want to exit the program? (Yes or no): ')
    if user_input.lower() == 'yes':
        exit()
