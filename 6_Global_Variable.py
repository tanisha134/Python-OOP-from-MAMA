#global Varible without Creating Object We can access as well...
class Student:
    #Global varible 
    School ='Onkur School'

    @classmethod
    def change_school(cls,new_school):
        cls.School = new_school # For Change the School

#Calling the Change_method
Student.change_school("BMS")
print(Student.School)


