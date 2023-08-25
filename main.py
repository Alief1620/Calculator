while True:
        try:
            number_1 = int(input("Enter a number 1:"))
            number_2 = int(input("Enter a number 2:"))
        except ValueError:
            print("Invalid literal sign")


        operators = input("Enter a operators: ")

        if operators == '+':
            print(f' Result: {number_1 + number_2}')
        elif operators == '-':
            print(f' Result: {number_1 - number_2}')
        elif operators == '*':
            print(f' Result: {number_1 * number_2}')
        elif number_2 == 0:
            print("is not divided into zero")
        elif operators == '/':
            print(f' Result: {number_1 / number_2}')
        else:
            print("Bad operator")
exit()




