a, b, c = ["Perry", "Donald", "Mickey"]
d, e, f = ["Platypus", "Duck", "Mouse"]

name = input("What's your name? ")

name = name.title()

print('| first | second |')
print('|-------|--------|')

def list():
    global perry,donald,mickey
    perry = (a,d)
    donald = (b,e)
    mickey = (c,f)
list()

match name:
    case "Perry":
        print(f"| {perry[0]} | {perry[1]} |")
    case "Donald":
        print(f"| {donald[0]} | {donald[1]} |")
    case "Mickey":
        print(f"| {mickey[0]} | {mickey[1]} |")
    case __:
        print(name)