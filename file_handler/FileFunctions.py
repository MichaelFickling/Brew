import json

def load_file(filename):
    with open(str(filename), "r") as Objects:
        dict1 = json.load(Objects)
        return dict1

def write_file(dict, filename):
    with open(str(filename), "w") as Objects:
        json.dump(dict, Objects)

def save_json(dict_people,dict_drinks):
    print(dict_people)
    write_file(dict_people, r"C:\Users\micha\PycharmProjects\myProject1\Drinks_+_Rounds_programme\PersonObjects")
    write_file(dict_drinks, r"C:\Users\micha\PycharmProjects\myProject1\Drinks_+_Rounds_programme\DrinksObjects")



