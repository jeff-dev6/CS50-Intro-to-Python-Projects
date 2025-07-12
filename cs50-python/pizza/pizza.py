import csv
import os
import sys
from tabulate import tabulate

def check_command_line():
    if len(sys.argv) < 2:
        print("Error: Too few command arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Error: Too many command arguments")
        sys.exit(1)
    else:
        return sys.argv[1]

def check_file(filename):
    if not filename.endswith(".csv"):
        print("Error: NOT A CSV FILE")
        sys.exit(1)
    if not os.path.isfile(filename):
        print(f"Error: THIS FILE {filename} DOES NOT EXIST")
        sys.exit(1)

def format_file(filename):
    with open (filename, "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        if not rows:
            print("Error: CSV FILE IS EMPTY")
            sys.exit(1)
        return (tabulate(rows, tablefmt="grid", headers="keys"))

def main():
    filename = check_command_line()
    check_file(filename)
    result = format_file(filename)
    print(f"{result}")

if __name__ == "__main__":
    main()






