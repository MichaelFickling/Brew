import time
from classes.ClassPeople import People, new_person
from classes.ClassDrinks import Drinks, new_drink
from classes.ClassOrders import Orders, reciepts
from file_handler.FileFunctions import load_file, save_json
from file_handler.SQL import save_people_to_database, load_from_database, save_drinks_to_database
from menu.menu import make_menu



def save_all():#for use later in programme
    save_drinks_to_database(List_of_drinks)
    save_people_to_database(List_of_people)

#create lists of objects and create the objects
def update_list_of_people(dict_people):
    pkeys = [*dict_people]
    for key in pkeys:
        List_of_people.append(People(key, dict_people[key]["age"], dict_people[key]["preference"]))
        return List_of_people
        #update(withdatabase)

def update_List_of_drinks(dict_drinks):
    dkeys = [*dict_drinks]
    for key in dkeys:
        List_of_drinks.append(Drinks(key, dict_drinks[key]["price"]))
        return List_of_drinks
        #update(withdatabase)

#initialise some variables
rounds = True
Reciepts_list=[]
List_of_people = []
List_of_drinks = []
List_of_orders = []
dict_people = {}
dict_drinks = {}


#load data from databases
drinks_data = load_from_database("drinks")
people_data = load_from_database("people")
order_data = load_from_database("orders")


#convert data into dictionaries
for person in people_data:
        dict_temp = {person[1] : {"age" : person[2], "preference" : person[3]}}
        dict_people.update(dict_temp)

for drink in drinks_data:
    dict_temp = {drink[1] : {"price":drink[2]}}
    dict_drinks.update(dict_temp)

List_of_drinks = update_List_of_drinks(dict_drinks)
List_of_people = update_list_of_people(dict_people)


# START MAIN MENU // MENU DECISION TREE
run = True
while run == True:
    User_selection = make_menu([
        "List all people",
        "List all drinks",
        "List people and their preferences",
        "List drinks and their prices",
        "New Entry",
        "Remove person",
        "Remove drink",
        "Make order",
        "exit",
        "print orders"])

    if User_selection == "1":
        for person in List_of_people:  # prints all object ages
            print(person.name)
        input("press enter to continue\n")

    elif User_selection == "2":
        for drink in List_of_drinks:  # prints all object ages
            print(drink.name)
        input("press enter to continue\n")

    elif User_selection == "3":#List people and preferences
        print("Person : Their preference\n")
        for person in List_of_people:  # prints all object ages
            print(f"{person.name} : {person.preference}")
        input("Press enter to continue")

    elif User_selection == "4":#List drinks and prices
        print("Drink : Price")
        for drink in List_of_drinks:
            print(f"{drink.name} : £{drink.price}")
        input("Press enter to continue")

    elif User_selection == "5":#make new entry
        choice = input("Would you like to add a new person[1] or new drink[2]? (or both)\n")
        a="false"
        if "1" in choice:
            a = "true"
            new_person(dict_people, List_of_people)
            save_all()
        if "2" in choice:
            new_drink(dict_drinks, List_of_drinks)
            save_all()
        elif a != "true":
            print("selection not recognised, returning to menu")
            time.sleep(1.5)
        print("updates made")
        time.sleep(1.5)

    elif User_selection == "6":  # remove from dict
        name_to_del = input("Enter name to remove from dictionary\n")
        if name_to_del not in dict_people:
            print("\nName not found, returning to menu\n")
            time.sleep(2)
            continue

        del dict_people[name_to_del]
        save_all()
        update_list_of_people(dict_people)
        print("Name removed from dictionary\n")
        time.sleep(1.5)
        continue

    elif User_selection == "7":  # remove from dict
        name_to_del = input("Enter name to remove from dictionary\n")
        if name_to_del not in dict_drinks:
            print("\nName not found, returning to menu\n")
            time.sleep(2)
            continue

        del dict_drinks[name_to_del]
        save_all()
        update_List_of_drinks(dict_drinks)
        print("Name removed from dictionary\n")
        time.sleep(1.5)
        continue

    elif User_selection == "8":
        if rounds == True:
            roundies = input("Who wants in on a round? (seperate with ',' )\n").capitalize().split(
                ",")  # user inputs the names of people who want to order
            print(f"People in the round: {roundies}\n")

            List_of_people_names=[]
            for person in List_of_people:
                a=person.name
                List_of_people_names.append(a.capitalize())


            for roundee in roundies:
                if roundee not in List_of_people_names:
                    if input(f"person {roundee} not found, would you like to add them to database? Y/N\n") == "Y":
                        new_person(dict_people, List_of_people)
                        save_all()

            Full_order=[]
            order_num = 1
            for person in List_of_people: # print out preferred drinks of known people, then ask what drinks people in the round want, then create order objects for each person.
                if person.name.capitalize() in roundies:
                    print("Drinks available")
                    print("Drink : Price")
                    i=0
                    for drink in List_of_drinks:
                        print(f"[{i}] {drink.name} : £{drink.price}")
                        i += 1
                    print(f"\n{person.name}'s preferences are : {person.preference}\n")  # print

                    drink_index =int(input(f"Which drink does {person.name} want? USE NUMBER\n")) # ask       this could ask for an input of pairs(person:drink pairs), rather than needing to go through a list in a specific order.
                    order_obj = Orders(person, List_of_drinks[drink_index])
                    order_num += order_num
                    Full_order.append(order_obj)#Full_order is a list of orders ... reciept
            time.sleep(2)


            Reciepts_list.append(reciepts(len(Reciepts_list), Full_order))

            if(input("Would you like a reciept yes [Y], no [N]\n").capitalize() == "Y"):
                print("reciept")
                for order in Full_order:
                  print(f"{order.person.name}: {order.drink.name} , £{order.drink.price}")
                a=str(Reciepts_list[-1].Total())
                print("total £" + a)

            input("Press enter to continue")


            # for drink in range(len(person.preference)):
            #     if person.preference[drink] in List_of_drinks:
            #         print(f"and he gets some {drink}")
            #     else:
            #        print("but there is none left")
            #        break
        else:
            print("Sorry we are not taking rounds right now")

    elif User_selection == "9":
        save_all()
        run = False

    elif User_selection == "10":
        for Reciept in Reciepts_list:
            for order in Full_order:
              print(f"{order.person.name}: {order.drink.name}, {order.drink.price}\n")
            print(f"total: {Reciept.Total}")


    else:
        print("\nPlease input an integer which is on the menu")
        time.sleep(1.8)



#goals
# a=orders(a,b,c)#create orders object with name[b], drink they want[c]  as attributes (and order identifier[a](maybe this is so you can add multiple names and drinks to objects, use tuples/dictionaries to store names and drinks pairs)))
# a.person.name == persons name
# a.drink.name == drinks name (drink they ordered)


#loopthrough object list and ask if each one has the name your looking for
#python list comprehension
# def search_List_of_current_objects(object):
#     for object in List_of_current_drinks:
#         if object == object.name:
#             return("object in List_of_current_objects")
#             break
#         else:
#             continue