import sys
if len(sys.argv) != 2:
    print("none\n")
    exit()

parameter = sys.argv[1]
text = input("What was the parameter?: ")

if text == parameter:
    print("Good job!")
else:
    print("Nope, sorry...")