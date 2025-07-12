def convert(text):
    "replace :) with 🙂 and :( with 🙁"
    return text.replace(":)", "🙂").replace(":(", "🙁")

def main():
    text = input()
    print(convert(text))

main()
