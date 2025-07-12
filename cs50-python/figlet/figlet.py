import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()


    available_fonts = figlet.getFonts()


    if len(sys.argv) == 1:
        font = random.choice(available_fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in available_fonts:
        font = sys.argv[2]
    else:
        sys.exit("Usage: python figlet.py [-f FONT_NAME]")

    figlet.setFont(font=font)


    user_text = input("Enter text: ")

    
    print(figlet.renderText(user_text))

if __name__ == "__main__":
    main()
