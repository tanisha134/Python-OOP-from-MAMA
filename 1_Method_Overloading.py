# Method Overloading using Default Arugment

class Math:
    # This is a method--> passing Argument
    def add(self, a, b=0, c=0):
        return a+b+c
    

# Creating an Object 
ADD = Math()

print("Summation of a = ",ADD.add(5))
print("Summation of a and b = ",ADD.add(10, 10))
print("Summation of a, b and c = ",ADD.add(10, 20,30))


    

