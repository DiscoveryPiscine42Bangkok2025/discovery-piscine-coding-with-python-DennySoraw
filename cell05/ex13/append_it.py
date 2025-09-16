import sys
count = len(sys.argv) - 1

if count > 0:
    for arg in sys.argv[1:]:
        if arg.endswith("ism"):
            continue
        word = arg + "ism"
        print(word)
else:
    print("none\n")