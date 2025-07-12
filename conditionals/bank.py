def value(greeting):
    "Determine the amount to the greeting"

    greeting = greeting.lower().strip()

    if greeting.startswith("hello"):
       return 0
    elif greeting.startswith("h"):
       return 20
    else:
        return 100

def main():
    "Prompt the user for a greeting"
    user_input = input("Greeting: ")
    print(f"${value(user_input)}")

if __name__ == "__main__":
    main()




