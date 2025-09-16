num = input("Give me a number: ")
check = num.isdigit()

if check is True:
    print("This number is an integer.")
else:
    print("This number is a decimal.")