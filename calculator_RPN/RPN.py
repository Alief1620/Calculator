stack = []
while True:
        user_str = input('Enter a numbers and operators separated by spaces: ')
        user_str = user_str.split()
        for token in user_str:
            if token.isdigit():
                stack.append(int(token))
            elif token in " '+', '-', '*', '/'":
                if len(stack) < 2:
                    print('Not enough operands for')
                    break
                x = stack.pop(0)
                y = stack.pop(0)
                match token:
                    case '+':
                        stack.append(x + y)
                    case '-':
                        stack.append(x - y)
                    case '*':
                        stack.append(x * y)
                    case '/':
                        if y == 0:
                            print('Division by zero is not allowed')
                            print(f'The last result: {x}')
                            stack.append(x)
                            exit()
                        stack.append(x / y)
            else:
                print('Invalid input:', token)
                break

        try:
            print(stack[0])
        except IndexError:
            print('Invalid literal sign in list index')

        ask_user_update_the_program = input('Do you want to make a calculation with the previous result? (Yes or No): ')
        if ask_user_update_the_program != 'yes':
            stack.clear()

        ask_user_to_continue = input('Do you want to continue? (Yes or No): ')
        if ask_user_to_continue != 'yes':
            exit()

