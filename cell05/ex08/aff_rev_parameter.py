import sys
count = len(sys.argv) - 1

if count > 2:
    reverse = sys.argv[1:][::-1]
    for i, arg in enumerate(reverse, start=1):
        print(f"{arg}")
else:
    print("none\n")
