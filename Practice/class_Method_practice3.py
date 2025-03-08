class girl:
    def putdata(self):

        self.name = input("Enter Your Name = ")
        self.age = int(input("Enter Your Age = "))
        self.home = input("Where Do You Live? = ")
        self.roll = input("Enter Your Roll Number = ")

    def show(self):
        print("\n")
        print(f"Name is = {self.name}\nAge is = {self.age}\nHome is = {self.home}\nRoll is = {self.roll}")

#Creating object
Information1 = girl()
Information1.putdata()
Information1.show()

        

    