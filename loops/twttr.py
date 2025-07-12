import sys
import string

def main():
    text = check_user_input()
    formatted_text = shorten(text)
    print(f"{formatted_text}")

def check_user_input():
        user_input = input().strip()
        print(f"Received Input: '{user_input}'")
        if not any(char.isdigit() for char in user_input) or not any(char in string.punctuation for char in user_input):
            print("Exiting due to number or punctuation")
            sys.exit(1)
        return user_input

def shorten(word):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in word if char not in vowels)


if __name__ == "__main__":
     main()


