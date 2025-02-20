name = input("What's your name? ")

name = name.title()

# if name == "Harry" or name == "Hermione" or name == "Ron":
    # print("Gryffndor")
# elif name == "Draco":
    # print("Slytherin")
# else:
    # print("Get out!!!")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")