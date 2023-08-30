# Example: 4 5 +

while True:
    user_str = input("Enter a operands and operators with space: ")
    user_str = user_str.split()
    try:
        operand_1 = int(user_str[0])
        operand_2 = int(user_str[1])
    except ValueError:
        print("Invalid literal sign")

    if user_str[2] == '+':
        print(f' Result: {operand_1 + operand_2}')
        user_input = input("Do you want to exit the program? (Yes or not): ")
        if user_input.lower() == "no":
            exit()
    elif user_str[2] == '-':
        print(f' Result: {operand_1 - operand_2}')
    elif user_str[2] == '*':
        print(f' Result: {operand_1 * operand_2}')
    elif user_str[2] == 0:
        print("is not divided into zero")
    elif user_str[2] == '/':
        print(f' Result: {operand_1 / operand_2}')
    else:
        print("Bad operator")
exit()


