#Constractor
class frinds:
    #global Variable
    School = "Aunkur Society Girl's High School"
    #Local Variable
    def __init__(self, name, home, roll, age):
        self.name = name
        self.home = home
        self.roll = roll
        self.age = age
    
    def show(self):
        print(f"Name is : {self.name} , Home is at : {self.home}, Roll Number is : {self.roll}, Age is : {self. age}, School is = {self.School}")

ha= frinds('sharodia','Muradpur', 23 , 14)
ha.show()

ha1= frinds('Tanisha','forida para',39,13)
ha1.show()

ha2 = frinds('Soha','khulna',11,14)
ha2.show()
