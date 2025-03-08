class Library:
    #Global Varible 
    Book=['ghost Story', 'Love story', 'funny Story']
    #Constractor
    def __init__(self, book_name, pages):
        self.book_name=book_name # instance attribute
        self.pages=pages # instance Attribute

        #conditiaon 
        if self.book_name in Library.Book:
            print(f"{self.book_name} is availbale in the Book list")
        else:
            print(f"{self.book_name} is not Available in the book List")

    #instanee method 
    def show(self):
        print(f"Book name : {self.book_name}, Number of Pages : {self.pages}")
        

print("----------Welcome to My Library--------------")
object1=Library('ghost Story', 100)
object2=Library('Hate story',25)
object3=Library('Love story', 100)
object4=Library('Break Up Story', 10)



