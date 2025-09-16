import sys
def shrink(text):
    if len(text) > 8:
        return text[:8]
    elif len(text) < 8:
        return text.ljust(8, 'z')

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        print(shrink(arg))
else:
    print("none\n")