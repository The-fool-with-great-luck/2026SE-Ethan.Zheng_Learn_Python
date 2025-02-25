def main():
    x = input("x = ? ").strip()
    operator = input("y = ? ").strip()
    z = input("z = ? ").strip()
    expression = f"{x} {operator} {z}"
    print(evaluate_expression(expression))

def evaluate_expression(expression):
    try:
        x, operator, z = expression.split()
        x, z = int(x), int(z)
        
        operations = {
            "+": x + z,
            "-": x - z,
            "*": x * z,
            "/": x / z
        }
        
        if operator not in operations:
            raise ValueError("Invalid operator")
        
        return f"{operations[operator]:.1f}"
    except ValueError:
        return "Error: Invalid input"
    except ZeroDivisionError:
        return "Error: Division by zero"

if __name__ == "__main__":
    main()
