def get_digit(n):
    while n > 0:
        digit = n % 10
        print(digit,)
        n //= 10

n = int(input('enter a number: '))
get_digit(n)