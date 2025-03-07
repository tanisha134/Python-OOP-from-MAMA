# class girl:
#     def putdate(self):
#         self.name = input("Enter Your Name : ")
#         self.roll = int(input("Enter Your Roll : "))

#     def show(self):
#         print(f"Name : {self.name}\nRoll : {self.roll}")



# # Creating a Object 
# a = girl()
# a.putdate()
# a.show()


class girl:
    def putdata(self):
        self.name = input("Enter Your Name ")
        self.home = input("Where do you live? ")
        self.age  = int(input("Enter your age = "))


    def show(self):
        print("\n")
        print("--------information-------------")
        print(f"Name is = {self.name}\nHome is = {self.home}\nAge is = {self.age}")

object1 = girl()
object1.putdata()
object1.show()