def indoorvoice(text):
    "converts texts to lowercase"
    return text.lower()

def main():
    #prompt user for input
    text = input().lower()
    print(indoorvoice(text))

main()



