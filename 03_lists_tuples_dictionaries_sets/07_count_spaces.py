text = input("Enter a string: ")
space_count = 0

for char in text:
    if char == " ":
        space_count += 1

print(f"Total spaces = {space_count}")        