#oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day. 
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''

import random

class Student:
    def __init__(self, name, year, major, gpa):
        self.name = name
        self.student_id = random.randrange(1, 1000, 1)
        self.year = year
        self.major = major
        self.gpa = gpa

    def honors(self):
        if self.gpa > 3.5:
            print("is eligible for the honors program!")

        else:
            print("does not qualify for the honors program.")


    def freeLunch(self, random_id):
        if random_id == self.student_id:
            print("Yay free lunch!")
        else:
            print("Loser!")

def main():
    student1 = Student("Dan", "Freshman", "Computer Science", 3.8)
    student2 = Student("Bob", "Sophomore", "Engineering", 3.2)
    student3 = Student("Joe", "Junior", "Biology", 4.0)

    random_id = random.randrange(1, 1000, 1)

    student1.freeLunch(random_id)
    student1.honors()

    student2.freeLunch(random_id)
    student2.honors()

    student3.freeLunch(random_id)
    student3.honors()


main()

