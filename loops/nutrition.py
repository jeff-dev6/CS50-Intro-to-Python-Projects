fruits_calories = {

             "Apple": 130,
             "Avocado": 50,
             "Banana": 110,
             "Cantaloupe": 50,
             "Grapefruit": 60,
             "Grape": 90,
             "Honeydew Melon": 50,
             "Kiwifruit": 90,
             "Lemon": 15,
             "Lime": 20,
             "Nectarine": 60,
             "Orange": 80,
             "Peach": 60,
             "Pear": 100,
             "Pineapple": 50,
             "Plums": 70,
             "Strawberries": 50,
             "Sweet Cherries": 100,
             "Tangerine": 50,
             "Watermelon": 80
}

def get_calories(fruits):
    if fruits in fruits_calories:
        return fruits_calories[fruits]
    else:
        return None


def main():
    fruit_input = input("Enter a fruit: ").title().strip()
    calories = get_calories(fruit_input)
    if calories is not None:
        print(f"{calories}")
    else:
        return None


if __name__ == "__main__":
    main()






