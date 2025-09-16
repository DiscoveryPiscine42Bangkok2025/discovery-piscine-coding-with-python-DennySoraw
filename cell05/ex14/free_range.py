import sys
count = count = len(sys.argv) - 1
if count != 2:
    print("none\n")
    exit()

num_1 = int(sys.argv[1])
num_2 = int(sys.argv[2])
print("[", end="")
for i in range(num_1, num_2+1):
    if i == num_2:
        print(f"{i}", end="")
    else:
        print(f"{i}", end=", ")
print("]")