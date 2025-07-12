def main():
    price = 50
    amount_due = price
    total_inserted = 0

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = get_coin()
        total_inserted += coin
        amount_due -= coin

    change_owed = total_inserted - price
    print(f"Change Owed: {change_owed}")


def get_coin():
    while True:
          coin = int(input("Insert a coin: "))
          if coin in [25, 10, 5]:
               return coin
          else:
               print("Invalid Coin Denomination, Amount Due: 50")

main()




