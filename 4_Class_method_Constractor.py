class girl:
    #Constractor
    def __init__(self, name , age, home):
        self.name=name
        self.age=age
        self.home=home


    # To show this function
    def show(self):
        print(f"Name is : {self.name} , Age is : {self.age} , Home is at : {self.home}")
        

hm=girl('safa', 13 , 'abashik')
hm.show()
hm1=girl('soha',14, 'Khulna')
hm1.show()
    
    
