
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
        
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.country} {self.code} {self.product} {self.cost} {self.quantity}"


#=============Shoe list===========

shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            next(file)
            for line in file:
                country, code, product, cost, quantity = line.strip().split(",")
                shoe_list.append(Shoe(country, code, product, float(cost), int(quantity)))
    except Exception as e:
        print("An error occurred:", e)

def capture_shoes():
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    cost = float(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))
    shoe_list.append(Shoe(country, code, product, cost, quantity))

def view_all():
    for shoe in shoe_list:
        print(shoe)

def re_stock():
    if not shoe_list:
        print("No shoes found. Please add shoes first.")
        return

    min_quantity = min(shoe.quantity for shoe in shoe_list)
    shoe_to_restock = next((shoe for shoe in shoe_list if shoe.quantity == min_quantity))
    print(f"The shoe with the lowest quantity is {shoe_to_restock.product}")
    restock_quantity = int(input("Enter the quantity to restock: "))
    shoe_to_restock.quantity += restock_quantity
    
    with open("inventory.txt", "r") as f:
        lines = f.readlines()
    with open("inventory.txt", "w") as f:
        for line in lines:
            shoe_data = line.strip().split(",")
            if shoe_data[1] == shoe_to_restock.code:
                shoe_data[4] = str(shoe_to_restock.quantity)
            f.write(",".join(shoe_data) + "\n")

def seach_shoe(code):
    for shoe in shoe_list:
        if shoe.code == code:
            return shoe
    return None


def value_per_item():
    total_value = 0
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        total_value += value
        print(f"{shoe.product}: {value}")
    print(f"Total value: {total_value}")

def highest_qty():
    max_quantity = max(shoe.quantity for shoe in shoe_list)
    highest_qty_shoe = next(shoe for shoe in shoe_list if shoe.quantity == max_quantity)

    print(f"The shoe with the highest quantity for sale is {highest_qty_shoe.product} with a quantity of {highest_qty_shoe.quantity}.")


#==========Main Menu=============

def main():
    while True:
        print("\nWelcome to the Shoe Inventory Management System")
        print("1. Read Shoes Data")
        print("2. Capture Shoes")
        print("3. View All Shoes")
        print("4. Re-Stock Shoes")
        print("5. Search for a Shoe")
        print("6. Calculate Value Per Item")
        print("7. Find the Shoe with the Highest Quantity")
        print("8. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            read_shoes_data()
        elif choice == 2:
            capture_shoes()
        elif choice == 3:
            view_all()
        elif choice == 4:
            re_stock()
        elif choice == 5:
            code = input("Enter shoe code: ")
            seach_shoe(code)
        elif choice == 6:
            value_per_item()
        elif choice == 7:
            highest_qty()
        elif choice == 8:
            break
        else:
            print("Invalid choice. Try again.")

main()
