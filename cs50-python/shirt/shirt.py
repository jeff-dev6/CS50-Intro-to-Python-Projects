from PIL import Image, ImageOps
import sys
import os

def check_command_line_argument():
    if len(sys.argv) < 3:
        print("Error: Too few command line argument")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Error: Too many command line argument")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]

def check_extension(input_path, output_path):

    allowed_extensions = [".jpg", ".jpeg" ".png"]

    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()

    if input_ext not in allowed_extensions or output_ext not in allowed_extensions:
        sys.exit("Error: input and output must be in 'jpg', 'jpeg', or 'png'")

    if input_ext != output_ext:
        sys.exit("Error: input and out must have same extention")

def main():
    input_path, output_path = check_command_line_argument()
    check_extension(input_path, output_path)

    try:
        input_image = Image.open(input_path)
    except FileNotFoundError:
        sys.exit("Input file does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    input_image = ImageOps.fit(input_image, size)
    input_image.paste(shirt, shirt)
    input_image.save(output_path)


if __name__ == "__main__":
    main()

