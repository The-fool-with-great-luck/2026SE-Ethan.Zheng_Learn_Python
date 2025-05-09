def main():
    x = int(input("Choose Num1 "))
    y = int(input("Choose Num2 " ))
    operator = (input("Choose Operator "))
    process()
    print(result)

def process():
    if operator == "-":
        result = x - y
    elif operator == "+":
        result = x + y
    elif operator == "*":
        result = x * y
    elif operator == "/":
        result = x / y
    else:
        result = 'unknown'


main()