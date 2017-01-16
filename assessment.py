"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   The three main design advantages that object orientation can provide are
   encapsulation, abstraction, and easy to make different types of a subject.
   Encapsulation allows the developer to control what is changeable and what is
   not such as hidden methods and attributes.
   With abstraction, a developer does not have to concern how the methods of a
   class work. The developer can just trust whatever is in the
   class is doing what it needs to do. Also, thanks to classes, the developer
   can make several different types of objects such as for class Animal, you can
   have a monkey object, cat object, etc.. that share certain attributes and
   each object can be tweeked to have specific attributes.

2. What is a class?

    A class is a blueprint/template for an object.

3. What is an instance attribute?

    A characteristic of a specific instance of a class.

4. What is a method?

    Methods are functions that are inside of a class. They are what perform the
    "actions" of the class.

5. What is an instance in object orientation?

    An instance is an individual object of a class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

    Class attribute can be applied to the whole class and every instance whereas
    an instance attribute is specific to a certain instance. An example of this
    would be for class Animals. A class attribute for that could be
    "the total number of animals in the world" and an instance attribute could
    be "vertebrates".

"""


# Parts 2 through 5:
# Create your classes and class methods

class Students(object):
    school = "Hogwarts"  # all students in this class go to Hogwarts

    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def get_avg_grade(self):
        """ Calculates the average grade of each student """
        total_points = 0
        for grade in self.grades:
            total_points = total_points + grade
        avg_grade = total_points/len(self.grades)
        return avg_grade

tom = Students('Tom', 12, [80, 90, 70])
print tom.name
print tom.age
print tom.school
print tom.grades
print tom.get_avg_grade()
