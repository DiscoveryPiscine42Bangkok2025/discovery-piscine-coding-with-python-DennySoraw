import sys
count = len(sys.argv) - 1
check = "z"
found = False

if count > 0:
    for arg in sys.argv[1:]:
        if arg == check:
            found = True
            break
        print(check, end="")
else:
    print("none\n")