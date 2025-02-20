number = input("What is the Great Question of life? ")

match number:
    case "42" | "fourty-two" | "fourty two":
        print("Yes")
    case _:
        print("No")