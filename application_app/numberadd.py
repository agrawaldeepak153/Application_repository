#friend_list = ["Akhil","Mohit","Prashant"]
#for friends in friend_list :
    #if friends==friend_list[2] :
        #print(f"{friends} my friend in office")
    #else :
        #print(f"{friends}  not my friend in office")
'''
import json

friend_age = {"Deepak": 35,"Akhil":24,"Mohit":25}
jsonlist = json.dumps(friend_age)
print(jsonlist)
print(friend_age["Akhil"])
'''
'''
def hellowPrint():
    print("Hellow")

hellowPrint()
'''
from audioop import avg
from unicodedata import name

class Student:
    def __init__(self,name,age = 40):
        self.student_name = name
        self.age = age
        self.number = [10,40,30,20,50]

    def averageNumber(self):
        sum = 0
        avg = 0
        for i in range(len(self.number)):
            sum += self.number[i]
        avg = sum / len(self.number)
        return int(avg)

_student = Student(name ="Deepak Singh")
print(f"Name of Student are : {_student.student_name} and Student Age is : {_student.age}")
print(f"Average of Num are : {_student.averageNumber()}")