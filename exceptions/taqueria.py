menu = {

    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
} #define menu dictionary

def ordered_list():
    total = 0.0 #initialize total

    while True:

        try:
        #Prompt user for an order, stripping extra spaces and capitalizing correctly
            order = input("Place an order: ").strip().title()
            price = menu.get(order) ## Returns None if item is not found

            if price is not None: #check if item is in menu
                total += price #add price to total
                print(f"Total: ${total:.2f}") #print formatted total

        except EOFError: #Detect Control-D
            print("\n") #print a new line
            break #exit loop

def main():
    ordered_list() #Start the ordering process


if __name__ == "__main__":
    main()

