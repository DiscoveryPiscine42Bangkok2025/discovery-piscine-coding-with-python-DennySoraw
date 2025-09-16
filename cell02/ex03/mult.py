num_1 = int(input("Enter the first number :"))
num_2 = int(input("Enter the second number :"))
result = num_1 * num_2
print(num_1,"x",num_2,"=",result)
if result == 0:
    print("The result is both positive and negative.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positve.")