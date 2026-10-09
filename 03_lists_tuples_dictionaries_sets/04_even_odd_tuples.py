numbers = (2, 3, 5, 6, 7, 9, 4)

even_number = []
odd_number = []

for n in numbers:
    if n % 2 == 0:
        even_number.append(n)
    else:
        odd_number.append(n)

even_tuple = tuple(even_number)
odd_tuple = tuple(odd_number)

print('even tuple = ', even_tuple )
print('odd tuple = ', odd_tuple )
