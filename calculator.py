#user input 
num1 = float(input("Enter a number: "))
op = (input("""
+ = +(add)
- = -(sub)
/ = /(div)
* = *(multi)

Enter operator: 
"""))
num2 = float(input("Enter a number: "))
#using the user input
if op == "+":
    print(float(num1 + num2))
elif op == "_":
    print(float(num1 - num2))
elif op == "/":
    print(float(num1 / num2))
elif op == "*":
    print(float(num1 * num2))
else:
    print("invalid operator")
    
    
    #free use
    #simple calculator 
