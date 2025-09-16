num_2 = 0
while num_2 <= 10:
    print("Table", num_2, ":", end=" ")

    num_1 = 0
    while num_1 <= 10:
        print(num_1 * num_2, end=" ")
        num_1 += 1
    
    print()
    num_2 += 1