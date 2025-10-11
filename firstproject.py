#firstProject: calculator

operator = input("Enter an operator: (+ - * /): ")
num1 = float(input("please enter your first number: "))
num2 = float(input("please enter your second number: ")) 

if operator == "+":
    total = num1 + num2 
    print(type(total))
elif operator == "-":
    total = num1 - num2
    print(round(total))
elif operator == "*":
    total = num1 * num2
    print(round(total))
elif operator == "/":
    total = num1 / num2
    print(round(total))
 