import sys
import os

def check_command_line():
        if len(sys.argv) < 2:
            print("Error: Too few command-line arguments")
            sys.exit(1)
        elif len(sys.argv) > 2:
            print("Error: Too many command-line arguments")
            sys.exit(1)
        else:
             return sys.argv[1]

def check_file(filename):
          if not filename.endswith(".py"):
               print("Not a Python file")
               sys.exit(1)
          if not os.path.isfile(filename):
               print(f"Error: The file '{filename}' does not exist")
               sys.exit(1)

def read_file(filename):
      with open (filename, "r") as file:
            count = 0
            content = file.readlines()
            for line in content:
                  if line.strip() and not line.strip().startswith("#"):
                        count += 1
            return count

def main():
      filename = check_command_line()
      check_file(filename)
      lines_of_code = read_file(filename)
      print(f"Line Of Code: {lines_of_code}")

if __name__ == "__main__":
      main()


