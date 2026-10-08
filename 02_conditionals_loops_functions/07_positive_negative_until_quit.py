while True:
    n = input("enter a number or enter Quit to terminate ")
    
    if n == 'Quit':
        break

    n = int(n)

    if n > 0:
        print('positive number ')
    else:
        print('negative number ')    
    