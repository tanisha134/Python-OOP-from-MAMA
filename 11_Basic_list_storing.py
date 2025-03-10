class Libray:
    def __init__(self):
        self.books = ['safa', 'hira'] #intance Attribute

    #for ordering the Book 
    def order_book(self, Book_name):
        if Book_name in self.books:
            return f"This {Book_name} is available in the Library sir, So your Order has been Placed  : "
        else :
            return f"This {Book_name} is not Available in the Library , Sorry sir !!!"
    # for adding a book 
    def add_books(self,Book_name):
        if Book_name not in self.books:
            self.books.append(Book_name)
            print(f"This {Book_name} is added Successfully ")
        else:
            print (f"This book is already in the Book list sir , So you can not add Sir <3")
    # For Removing a book
    def remove_book(self,Book_name):
        if Book_name in self.books:
            self.books.remove(Book_name)
            print(f"This {Book_name} is Deleted from the Library Sir")
        else:
            print(f"This {Book_name} is not available in the Library, So You can not remove Sir <3")
    # For Showing the Book List
    def view_books(self):
        if self.books:
            print("The Book list are :",' , '.join(self.books))

        
    # For Taking form user Input
    def user_choise(self):
        while True:
            self.view_books()
            print("\n===Welcome to my Library=======")
            print("1. <=Order a book :=> ")
            print("2. <=Add a new book sir :=> ")
            print("3. <=Remove a book :=> ")
            print("4. <=Exit:=> ")
            choice=input("Enter Any option sir among (1,2,3 and 4) : ").strip()
            if choice == "1":
                book_name =input("Enter The Book name that You want to order sir : ").strip().lower()
                print(self.order_book(book_name))
            elif choice == "2":
                book_name =input("Enter a new book that you want to add sir <333 : ").strip().lower()
                self.add_books(book_name)
            elif choice == "3":
                book_name =input("Enter a book that you want to Remove sir <333 : ").strip().lower()
                self.remove_book(book_name)
            elif choice =="4":
                print("Thank you sir For Visiting Our Library <3")
                break
            else:
                print("Please Enter a valied Option among 1,2 and 3 Sir !!")



store = Libray()
store.user_choise()
        
            
        
