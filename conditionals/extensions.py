def extension(file):
    "Determine the file media type based on the suffix of the file name."

    file = file.lower().strip()

    if file.endswith(".gif"):
        return ("image/gif")
    elif file.endswith(".jpg"):
        return ("image/jpeg")
    elif file.endswith(".jpeg"):
        return ("image/jpeg")
    elif file.endswith(".png"):
        return ("image/png")
    elif file.endswith("pdf"):
        return ("application/pdf")
    elif file.endswith(".txt"):
        return ("text/plain")
    elif file.endswith(".zip"):
        return ("application/zip")
    else:
        return ("application/octet-stream")


def main():
    name = input("Enter name of file: ")
    print (extension(name))

main()
