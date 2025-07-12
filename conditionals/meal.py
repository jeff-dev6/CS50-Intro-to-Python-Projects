def get_user_input():
        user_input = input("What's the time? ")
        return user_input

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    converted_time = hours + (minutes/60)
    return converted_time

def meal_time(time):
    if 7.00 <= time <= 8.00:
        return "breakfast time"
    elif 12.00 <= time <= 13.00:
        return "lunch time"
    elif 18.00 <= time <= 19.00:
        return "dinner time"
    else:
        return None

def main():
     try:
          user_input = get_user_input()
          converted_input = convert(user_input)
          display_message = meal_time(converted_input)
          print(f"{display_message}")
     except ValueError:
          print("Invalid input format: Try Again!")

if __name__ == "__main__":
    main()
