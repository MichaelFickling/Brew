import unittest
from unittest.mock import patch


# with mock.patch("builtins.input", return_value="")
# with mock.patch("builtins.input", return_value="")
# with mock.patch("builtins.input", return_value="")


def new_person():
    name = input("Please enter the name of person you would like to update (new names will make a new entry)\n")
    age = input("enter new age\n")
    preference = input("enter new preference\n")
    dict_temp = {name: {"age": age, "preference": preference}}
    #dict_people.update(dict_temp)
    return dict_temp

    #List_of_people.append(People(name, age, preference))  # add new object to our list
    #print(List_of_people)#prints names of all objects


class RunTest(unittest.TestCase):

    name = "michael"
    age = 22
    preference = "coke"

    @patch('builtins.input', side_effect=[name, age, preference])
    def test_new_person(self):
        result = new_person()
        self.assertTrue(result == {name: {"age":age, "preference":preference}})
