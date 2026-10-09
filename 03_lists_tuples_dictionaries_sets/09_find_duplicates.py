numbers = [1, 2, 3, 2, 4, 1, 5, 2]

duplicate = set()

for num in numbers:
    if numbers.count(num) > 1:    # count() tells us how many times a value appears in a list.
        duplicate.add(num)

print(duplicate)        