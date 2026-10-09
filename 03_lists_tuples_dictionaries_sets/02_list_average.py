# Given a list of integers compute the average of all numbers in the list.
numbers = [5, 28, 12, 41, 8, 19]

total = sum(numbers)
count = len(numbers)

average = total / count

# Display the average rounded to 3 decimal places
print(f'average of {numbers} = {average:.3f}') 