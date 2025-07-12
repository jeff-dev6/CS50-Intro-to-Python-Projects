def main():
    name = input("Enter a name of a variable in Camel Case: ")
    print (camel_to_snake(name))


def camel_to_snake(camel_case):
    snake_case = camel_case
    for char in camel_case:
        if char.isupper():
            snake_case = snake_case.replace(char, "_" + char.lower())
    if snake_case.startswith("_"):
            snake_case = snake_case[1:]

    return snake_case

main()
