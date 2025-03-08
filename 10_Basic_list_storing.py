class Library:
    #Empty varible
    Book =[]

    #Constrctor 
    def __init__(self, Book_Name , pages):
        self.Book_name =Book_Name #instace Attribute
        self.pages =pages #intacence attribte 

        #Condition 
        if self.Book_name not in self.Book:
            self.Book.append(self.Book_name)
            
    #instace Method
    def show(self):
        print(f"Book name is :  {self.Book_name} and Number of Pages are : {self.pages}")
        
object1=Library('Break Up Story ', 20)
object2=Library('hate Story', 100)

# this is called Details
# print(object1.__dict__)
# print(object2.__dict__)

object1.show()