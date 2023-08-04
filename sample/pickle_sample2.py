# This is a simple tutorial to show an example for pickle serialization
import pickle

class Person:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def print_info(self):
        print(self.name)
        print(self.age)
        print(self.weight)

    def get_older(self, years):
        self.age +=years

# Person Data to be stored - Run this commented code first generate the binary file
# p1 = Person('mike', 50, 80)
# p1.print_info()
# p1.get_older(2)
# p1.print_info()

# Write the Person data to a binary file with serialization(You will notice a binary file got created)
# with open('mike.pickle', 'wb') as f:
#     pickle.dump(p1, f)

# Now read/load the stored serialized Person data from pickle
with open('mike.pickle', 'rb') as f:
    p1 = pickle.load(f)

p1.print_info()