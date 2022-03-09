print('Hello users. You r welcome to my first project Calculator')
num1 = float(input('Print your first num: '))
num2 = float(input('Print your second num: '))
process_with_num = input('What proccess do you want to do: \n +, -, *, **, /, //, % \n: ')
if process_with_num == "+":
    print("result: ",num1 + num2)

elif process_with_num == "-":
    print("result: ",num1 - num2)
elif process_with_num == "*": 
    print("result: ",num1 * num2)
elif process_with_num == "/":
    print("result: ",num1 / num2)
elif process_with_num == "**":
    print("result: ",num1 ** num2)
elif process_with_num == "//":
    print("result: ",num1 // num2)
elif process_with_num == "%":
    print("result: ",num1 % num2)
else: 
    print('This function is unavailable')