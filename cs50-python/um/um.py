import re


def main():
    s = input("Enter a Sentence ")
    print(count(s))


def count(s):
    pattern = (

        r"\bum\b[,.?!]?"
    )

    match = re.findall(pattern, s, re.IGNORECASE)

    return len(match)


if __name__ == "__main__":
    main()
