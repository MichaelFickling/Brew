class People:
    def __init__(self, name, age, preference):
        self.name = name
        self.age = age
        self.preference = preference

    def __repr__(self):
        return self.name

    def attributes(self):
        attributes_list = ["name", "age", "preference"]
        return attributes_list

def new_person(dict_people, List_of_people):
    run = True
    while run == True:
        name = input("Please enter the name of person you would like to update (new names will make a new entry)\n")
        age = input("enter new age\n")
        preference = input("enter new preference\n")
        dict_temp = {name: {"age": age, "preference": preference}}
        dict_people.update(dict_temp)

        List_of_people.append(People(name, age, preference))  # add new object to our list
        print("Current list of people")

        print(List_of_people)#prints names of all objects
        if input("Would you like to add another person? yes[Y], no[N]\n").capitalize() == "Y":
            run = True
        else:
            run = False