import unittest
from classes.ClassPeople import People
# def sum(a,b):
#     return a + b

def Testperson(name, age, preference): #function to create an object//this is an example function
    return People(name, age, preference)


class RunTest(unittest.TestCase):# test class People creates object

    def setUp(self):
        self.expected_name = "alfred"
        self.expected_age = 82
        self.expected_preference = "wine"
        self.Testperson = People(self.expected_name, self.expected_age, self.expected_preference)

    def test_object_name(self):
        self.assertEqual(self.Testperson.name, self.expected_name)

    def test_object_age(self):
        self.assertEqual(self.Testperson.age, self.expected_age)

    def test_object_preference(self):
        self.assertEqual(self.Testperson.preference, self.expected_preference)






