#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        return f"Cost: R{self.cost}"
        

    def get_quantity(self):
        return f"Quantity: {self.quantity}"
        

    def __str__(self):
        return f"Shoe Code: {self.code}, Country: {self.country}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"
        


#=============Shoe list===========

shoe_list = []

#==========Functions outside the class==============

def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as inventory:
            lines = inventory.readlines()[1:]   #To exclude the first line
            for line in lines:
                details = line.strip().split(',')
                shoe = Shoe(details[0], details[1], details[2], int(details[3]), int(details[4]),)  #Cast as cost and quantity as int
                shoe_list.append(shoe)
    except Exception as e:
        print("The error is: ",e)

def capture_shoes():
    print("Specify the details regarding the pair of shoes.\n")
    country = input("Country: ")
    code = input("Shoe Code: ")
    product = input("Product Name: ")
    cost = int(input("Cost: "))
    quantity = int(input("Quantity: "))

    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)

    # Not specifically required but makes sense to also add the new pair of shoes to the text file 
    with open("inventory.txt", 'w') as file:
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

def view_all():
    for shoe in shoe_list:
        print(Shoe.__str__(shoe))

def re_stock():
    lowest_quantity_shoe = min(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"Lowest quantity shoe: {lowest_quantity_shoe.product} ({lowest_quantity_shoe.quantity} pairs)")

    choice = input("Do you want to increase the quantity? (y/n): ")
    if choice.lower() == 'y':
        added_quantity = int(input("Enter the added quantity: "))
        lowest_quantity_shoe.quantity += added_quantity

        with open("inventory.txt", 'w') as file:
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

def search_shoe():
    code = input("Please enter the code of the shoe: ")
    for shoe in shoe_list:
        if shoe.code == code.upper():
            print(Shoe.__str__(shoe))
            return
    print("Shoe not found.")

def value_per_item():
    for shoe in shoe_list:
        total_cost = shoe.cost * shoe.quantity
        print(f"The total cost for {shoe.product} is: R{total_cost}")

def highest_qty():
    max_quantity_shoe = max(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"FOR SALE!:\n{max_quantity_shoe.product}\n ")
  

#==========Main Menu=============
while True:
    read_shoes_data() #Call function to add data from text file to shoe_list
    print(
'''
Welcome to Nike Warehouse! Please select one of the options below.

    1. View all
    2. Add item
    3. Re-stock lowest-quantity item
    4. Search item
    5. View total value per item
    6. View highest-quantity item
    7. Exit
''')


    choice = int(input(": "))
    if choice == 1:
        view_all()
    
    elif choice == 2:
        capture_shoes()
    
    elif choice == 3:
        re_stock()
    
    elif choice == 4:
        search_shoe()
    
    elif choice == 5:
        value_per_item()
    
    elif choice == 6:
        highest_qty()
    
    elif choice == 7:
        print("Goodbye!")
        break

    else:
        print("Invalid selection. Please try again.")