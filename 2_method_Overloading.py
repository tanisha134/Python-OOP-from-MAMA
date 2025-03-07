class math:
    def add(self, *args):
        return sum(args)
    
#creating object
ADD=math()

print(ADD.add(5))
#method Overloadig
print(ADD.add(5, 10, 20))
#method Overloadig
print(ADD.add(5, 20, 30 , 40))
#method Overloadig
print(ADD.add(5, 20, 10 , 10 , 2, 1, 10))
    