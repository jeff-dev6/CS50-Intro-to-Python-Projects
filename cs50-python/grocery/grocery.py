def my_groceries():
    groceries_list = {}
    while True:
        try:
           items = input().strip().upper()
           if items:
                groceries_list[items] = groceries_list.get(items, 0) + 1
        except EOFError:
           print("\n")
           return groceries_list

def main():
     groceries = my_groceries()
     for item in sorted(groceries):
         print(f"{groceries[item]} {item}")

if __name__ == "__main__":
    main()









