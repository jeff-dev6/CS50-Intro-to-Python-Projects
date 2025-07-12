from validator_collection import validators, checkers, errors

def main():
    email = input("Enter your Email: ")
    try:
       validators.email(email)
       print("Valid")
    except errors.InvalidEmailError:
        print("Invalid")

if __name__ == "__main__":
    main()

