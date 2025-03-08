
class Math:
    # This is a method--> passing Argument
    def add(self, a, b=1, c=2,d =0):
        return a+b+c+d
    

# Creating an Object 
ADD = Math()

print("Summation of a = ",ADD.add(6))
#method Overloadig
print("Summation of a and b = ",ADD.add(20, 20))
#method Overloadig
print("Summation of a, b and c = ",ADD.add(2, 60,20)) 
#method Overloding
print("Summation of a, b, c and d =", ADD.add(20,30,40,50))