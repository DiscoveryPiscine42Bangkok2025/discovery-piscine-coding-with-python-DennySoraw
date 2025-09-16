import sys
count = len(sys.argv) - 1

if count > 0:
    print(f"parameters: {count}")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{arg}: {len(arg)}")
else:
    print("none\n")
