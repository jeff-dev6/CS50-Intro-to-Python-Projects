def playback(text):
    "replace spaces with '...' in the text"
    return text.replace(" ", "...")

def main():
    text = input().replace(" ", "...")
    print(playback(text))

main()

