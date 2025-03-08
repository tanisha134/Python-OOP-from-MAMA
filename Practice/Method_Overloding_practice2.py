class math:
    def add(self, *args):
        return sum(args)
    
#creating object
ADD=math()

print(ADD.add(10))
#method Overloadig
print(ADD.add(15, 20, 25))
#method Overloadig
print(ADD.add(25, 30, 35 , 40))
#method Overloadig
print(ADD.add(15, 20, 10 , 10 , 20, 31, 30))