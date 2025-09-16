def greetings(text=None):
    if text is None:
        print("Hello, noble stranger.")
    elif str(text).isdigit():
        print("Error! It was not a name.")
    else:
        print("Hello, "+ text + ".")

greetings("Alexandra")
greetings("Wil")
greetings()
greetings(42)