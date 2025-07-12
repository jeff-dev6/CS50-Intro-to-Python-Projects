def Energy(mass):
    "return energy as an interger using E = mc^2"
    c = 300000000
    return mass*(c ** 2)

def main():
    user_input = int(input("Enter the mass(Kg): " ))  #prompt the user for mass in Kilogram
    energy = (Energy(user_input))  #call the function
    print(int(energy)) #print energy as an interger

main()





