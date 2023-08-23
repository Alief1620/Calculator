number_1 = int(input("Enter a number 1: "))
number_2 = int(input("Enter a number 2: "))
operators = input("Enter a operators: ")
if operators == '+':
    print(number_1 + number_2)
elif operators == '-':
    print(number_1 - number_2)
elif operators == '*':
    print(number_1 * number_2)
elif number_2 == 0:
    print("is not divided into zero")
elif operators == '/':
    print(number_1 / number_2)
else:
    print("Bad operator")
