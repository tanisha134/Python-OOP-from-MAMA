class girl:
    # Global Variable
    School = 'Ankur School'
    #Constractor
    def __init__(self, name , age, home ):
        # local Variable
        self.name=name
        self.age=age
        self.home=home
        


    # To show this function
    def show(self):
        print(f"Name is : {self.name} , Age is : {self.age} , Home is at : {self.home} , Schol is : {self.School}")
        

hm=girl('safa', 13 , 'abashik')
hm.show()
hm1=girl('soha',14, 'Khulna')
hm1.show()
hm2=girl('Tanisha', 11, 'Mugultuli')
hm2.show()
    
    
