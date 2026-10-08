# Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print(n)