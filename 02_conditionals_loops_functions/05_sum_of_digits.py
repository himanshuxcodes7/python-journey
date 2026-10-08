#return the value of sum of the digits
def sum_digits(n):
    s = 0
    while n > 0:
        digit = n % 10
        s += digit
        n //= 10

    return s

n = int(input('enter a number: '))
s = sum_digits(n)
print("sum of digits = ", s)    