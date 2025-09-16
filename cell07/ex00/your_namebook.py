def array_of_names(namebook):
    names = []
    for f_name, l_name in namebook.items():
        name = f"{f_name.capitalize()} {l_name.capitalize()}"
        names.append(name)
    return names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}
print(array_of_names(persons))