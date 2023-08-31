# Example: 4 5 +
user_str = input("Enter a numbers and operands with space: ")
user_str = user_str.split()
print(user_str)
def my_function(x, y, operator):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == 0:
        print('is not divided into zero')
    elif operator == '/':
        return x / y
    user_input = input('Do you want to exit the program? (Yes or not): ')
    if user_input.lower() == 'no':
        exit()




























