import sys

def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False

    if not s[:1].isalpha():
        return False


    if not s.isalnum():
        return False

    seen_digit = False
    for i, char in enumerate(s):
        if char.isdigit():
           if not seen_digit:
                if char == "0":
                    return False
                seen_digit = True
           elif not char.isdigit():
               return False
        elif seen_digit:
            return False
    return True

def main():
    plate = input("Enter a valid Plate Number: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
        sys.exit(1)

if __name__ == "__main__":
    main()




