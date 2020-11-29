class Drinks:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return self.name

    def attributes(self):
        attributes_list = ["name", "price"]
        return attributes_list

def new_drink(dict_drinks, List_of_drinks):
    run = True
    while run == True:
        name = input("Please enter the name of drink you would like to update (new names will make a new entry)\n")
        price = float(input("Enter new price\n"))
        dict_temp = {name: {"price": price}}
        dict_drinks.update(dict_temp)

        List_of_drinks.append(Drinks(name, price)) # add new object to our list
        print("Current list of drinks")
        print(List_of_drinks)  # prints names of all objects
        if input("Would you like to add another drink? yes[Y], no[N]\n").capitalize() == "Y":
            run = True
        else: run = False

