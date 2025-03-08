class Library:
    #Constractor
    def __init__(self):
        self.books=['ghost story', 'love story', 'funny story']

    #instance method
    def order_book(self, book_name):
        if book_name in self.books:
            return f"{book_name} is availbale in the Book list"
        else:
            return f"{book_name} is not Available in the book List Sorry sir !!! <3"
            
store = Library()
book_name = input("Enter your Book name that you are Looking for : ").strip().lower()
print(store.order_book(book_name))
    
        

