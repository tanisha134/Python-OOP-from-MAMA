#Constractor
class frinds:
    def __init__(self, name, home, roll, age):
        self.name = name
        self.home = home
        self.roll = roll
        self.age = age
    
    def show(self):
        print(f"Name is : {self.name} , Home is at : {self.home}, Roll Number is : {self.roll}, Age is : {self. age}")

ha= frinds('sharodia','Muradpur', 23 , 14)
ha.show()

ha1= frinds('Hira mama','forida para',10,26)
ha1.show()
