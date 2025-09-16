import sys
count = len(sys.argv) - 1

if count != 1:
    print("none\n")
else:
    print(sys.argv[1].lower(), end="\n")