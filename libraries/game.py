import random

def main():
    level = get_level()
    secret_number = random.randint(1, level)
    guess_number(secret_number)


def get_level():
    while True:
        try:
            n = int(input("Enter Level: "))
            if n > 0:
                return n
        except ValueError:
            pass

def guess_number(secret):
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess > 0:
                if guess < secret:
                    print("Too small!")
                elif guess > secret:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
        except ValueError:
            pass

if __name__ == "__main__":
    main()






