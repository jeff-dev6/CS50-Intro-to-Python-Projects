import emoji

def main():
    text = input("Enter a str with emoji codes: ")
    emoji_text = emoji.emojize(text, language='alias')
    print(f"{emoji_text}")

if __name__ == "__main__":
    main()
