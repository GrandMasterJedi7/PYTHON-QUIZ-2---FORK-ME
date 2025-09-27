#Python Quiz 2
#Fork this repository to your own GitHub account and complete the following tasks in the pythonquiz2.py file.

#Submit a URL link to your completed repository ON GITHUB on Moodle. 

#variables: show an example of variable assignment and usage. Be sure to print the variable to demonstrate its value.

#data types: demonstrate at least three different data types (e.g., integer, string, list) and print their types using the type() function.


#functions: define a simple function that takes an argument and returns a value. Call the function and print the result.



#classes: create a simple class with an __init__ method and one other method. Instantiate the class and call the method, printing the result.

quiz = "Question 1"
print(quiz)
def type():
    type1 = int(32)
    print(f'{type1}')
    type2= [1, 2, 3, 4, 5]
    print(f'{type2}')
    type3 = "These are three data types: An integer, an array, and a string"
    print(f'{type3}')
def birthday():
    month = input("What month were you born?")
    day = int(input("What day were you born?"))
    age = float(input('How old are you?'))
    year = 2025 - age
    print(f'You were born on {month} {day}, {year}')
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f'Hi my name is {self.name}!')
myname = Person('Jase')
type()
birthday()
myname.greet()



