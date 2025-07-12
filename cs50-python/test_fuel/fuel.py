def main():
     fraction = input("Enter a fraction: ")
     percentage = convert(fraction)
     print(gauge(percentage))

def convert(fraction):
    split_fraction = fraction.strip().split("/")
    if len(split_fraction) != 2:
       raise ValueError("Not a valid fraction format")

    try:
        x = int(split_fraction[0].strip())
        y = int(split_fraction[1].strip())
    except ValueError:
         raise ValueError("x and y are not integer")

    if y == 0:
            raise ZeroDivisionError("Denominator can not be zero")

    if x > y:
            raise ValueError("Numerator can not be greater than Denominator")

    percentage = round((x / y) * 100)
    if 0 <= percentage <= 100:
        return percentage

def gauge(percentage):
     if percentage <= 1:
          return "E"
     elif percentage >= 99:
          return "F"
     else:
          return f"{percentage}%"

if __name__ == "__main__":
     main()









