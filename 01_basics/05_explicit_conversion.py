# The user enters a string containing a number. Convert it to:
# • an integer
# • a float
# • a string again
# Print all three values with their types.

a = input("enter a number: ")

i = int(a)
f = float(a)
s = str(a)

print("integer = ", i, type(i))
print("float = ", f, type(f))
print("String = ", s, type(s))
