
# In previous code, init and display both arnt adding any behaviour 
# So we'll try adding some behaviour to the previous code

class Student:
    def __init__(self, roll_no, name, total):         
        self.roll_no = roll_no                
        self.name = name                  
        self.total = total

    def display(self):                        
        print(self.roll_no, self.name, self.total)

    def result(self):   # <-- This represents the behaviour of that particular student
        if (self.total > 120):
            print('pass')
        else: 
            print('fail')


s0 = Student(0, 'Bhawesh', 100)
s0.display()
s0.result()


s1 = Student(1, 'Rahul', 150)
s1.display()
s1.result()


# The difference btw funciton and method is:
# When any function belongs to a class then that particular funtion is referred as methods 