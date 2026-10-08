#Letʼs create a Simple calculator that performs arithmetic operations. Create a function calculator(a, b, operation) that performs addition, subtraction,
# multiplication, or division based on the parameter.

def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    else:
        return "invalid operation"

a = int(input('enter value for a: '))
b = int(input('enter value for b: '))
operation = input('enter operation (+, -, *, /): ')

result = calculator(a, b, operation)

print('Result =', result)
    
