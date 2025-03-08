''''
Method ==> 4 types of Method
===================================
1) Instance Method 
2) Class method
3) Static method 
4) Regular Method
'''

# Regular method 
def final():
    print("Welcome To My daily Blog Guyes")

class student:
    #Gloval Varible or Gloval Attribute
    school = 'Ankur School'
    #Creating Constractor 
    def __init__(self, name , age):
        self.name =name #instace attribute
        self.age=age #instance Attribute
    
    #Intance Method (1 Number method)
    def display_info(self):
        print(f"Name : {self.name} , Age : {self.age} , School : {self.school} , Location : {self.locaiton}")
    
    #Class method (2 Number Method)
    @classmethod
    def change_school(cls, new_school, location):
        cls.school=new_school
        cls.locaiton = location

    #Static method   
    @staticmethod
    def add_numbers(a,b):
        return a+b

#Regular Method Calling 
final()

# For Changing the Scool
student.change_school('Nasibar Girls School', '2 Number gate')

#Creating Object for Student Class
student1=student('Tanisha', 13)
student1.display_info()
student2=student("Safa", 14)
student2.display_info()

print("......This is Static method......")
#for static method
object=student.add_numbers(10, 20)
print("The Summation of two Numbers is : ",object)

