import sys
count = len(sys.argv) - 1

if count >= 2:
    check = sys.argv[1]
    phrase = sys.argv[2]
    check_count = 0

    word = phrase.split()
    for text in word:
        if text == check:
            check_count += 1
    print(check_count)
else:
    print("none\n")