def operations(n1 , operator , n2):
    if operator == "+":
        return n1 + n2 
    elif operator == "-":
        return n1 - n2
    elif operator == "*":
        return n1 * n2
    elif operator == "/":
        if n2 != 0:
            return n1 / n2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator entered (+, -, *, /)."


try:
    n1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    n2 = float(input("Enter second number: "))

    result = operations(n1 , operator , n2)

    print(f"{n1} {operator} {n2} = {result}")

except ValueError:
    print("Error: Invalid input. Please enter numeric values for numbers.")
