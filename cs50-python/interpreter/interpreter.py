def interpreter(x, y, z):
    "calculate the arithmetic expression formatted as x, y, z"

    #calculate the arithmetic expression based on the operator
    if y == "+":
        calculate = x + z
    elif y == "-":
        calculate = x - z
    elif y == "*":
        calculate = x * z
    elif y == "/":
        if z != 0:
            calculate = x / z
        else:
            return "Error: Division by 0 is invalid"

    return f"{calculate:.1f}" #return calculated result as a one decimal float


def main():
    #prompt the user for an arithmetic expression
    user_input = input("Enter an expression: ")

    x, y, z = user_input.split()  #split the user input

    #convert x and z to intergers
    x = int(x)
    z = int(z)

    print(interpreter(x, y, z)) #print the formatted result


main()
