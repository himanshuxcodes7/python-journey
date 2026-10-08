salary = int(input("Enter salary: "))

if salary < 30000:
    tax_rate = 5
elif salary <= 70000:
    tax_rate = 15
else:
    tax_rate = 25

print("Final tax rate = ", tax_rate, "percent")    