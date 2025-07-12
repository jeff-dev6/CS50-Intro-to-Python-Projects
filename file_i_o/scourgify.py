import csv
import sys
import os

def check_command_line():
    if len(sys.argv) < 3:
        print("Error: Too few command line argument")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Error: Too many command line argument")
        sys.exit(1)
    else:
        return sys.argv[1], sys.argv[2]

def check_file(filename):
    if not filename.endswith(".csv"):
        print("Error: This is not a CSV File!")
        sys.exit(1)
    if not os.path.isfile(filename):
        print(f"Error: This file '{filename}' does not exist!")
        sys.exit(1)
    return filename

def format_file(input_file, output_file):
    with open (input_file, "r") as r, open (output_file, "w", newline="") as w:
        reader = csv.DictReader(r)
        writer = csv.DictWriter(w, fieldnames=["first","last","house"])
        writer.writeheader()
        for row in reader:
                last, first = row["name"].strip().split(",")
                writer.writerow({
                    "first": first.strip(),
                    "last": last.strip(),
                    "house": row["house"].strip()
                })

def main():
   input_file, output_file = check_command_line()
   check_file(input_file)
   format_file(input_file, output_file)

if __name__ == "__main__":
    main()
