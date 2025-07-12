user_input = input("What is the answer to the Great Question of Life, the Universe and Everything? " ).lower().strip()

if not (user_input == "42" or user_input == "forty two" or user_input == "forty-two"):
    print("No")
else:
    print("Yes")


