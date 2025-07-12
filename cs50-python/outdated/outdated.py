months = [

    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
       user_input = input("Enter Date: ").strip()
       formatted_date = convert_date(user_input)
       if formatted_date:
          print(formatted_date)
          break
       else:
          print("Invalid Date Format. Please Try Again: ")

def convert_date(date):
   #format date in MM/DD/YY
   try:
      if "/" in date:
         month, day, year = date.split("/")
         month, day, year = int(month), int(day), int(year)
      else:
         parts = date.replace("," , "").split()
         if parts[0] in months:
            month = months.index(parts[0]) + 1
            day, year = int(parts[1]), int(parts[2])
         else:
            return None

      if 1 <= month <= 12 and 1 <= day <= 31:
         return f"{year:04}-{month:02}-{day:02}"
   except (ValueError, IndexError):
      return None

if __name__ == "__main__":
   main()














