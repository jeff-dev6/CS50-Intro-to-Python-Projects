import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        tries = 0
        while tries < 3:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1
        if tries == 3:
            print(f"{x} + {y} = {correct_answer}")
    print(f"Score: {score}")



def get_level():
     while True:
        try:
            level = int(input("Enter Level: "))
            if level in [1,2,3]:
                return level
            else:
                continue
        except ValueError:
            continue

def generate_integer(level):
    if level not in [1,2,3]:
        raise ValueError
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
