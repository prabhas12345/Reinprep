#Que 1
#Vehicle Premium Amount
'''
class Fun():
    def __init__(self,vehicle_id,type1,cost,pre_amount):
        self.__vehicle_id=vehicle_id
        self.__type1=type1
        self.__cost=cost
        self.__pre_amount=pre_amount

    def get_func(self):
        if(self.__type1=="two wheelers"):
            pre_amount=(2/100)*self.__cost
            
        elif(self.__type1=="Four wheelers"):
            pre_amount=(6/100)*self.__cost
        else:
            pre_amount="error"
        return pre_amount
    def set_func(self):
        print(self.__pre_amount)
    def display(self):
        print("the vehicle details are",self.__type1)
 
F1=Fun(50,"wheelers",100,0)
print(F1.get_func())
F1.display()
'''

#Que 2

'''#A university wants to automate their addmission process.
students are admitted based on marks scored in a qualifying exam.
 A student is identified by student id,age,marks in qualifying exam
data are valid,if :
        # age is greater than 20
          marks is between 0 to 100(both inclusive)
          A student qualifies for admission,if
          age and marks are valid and marks is 65 or more
----------------------------------------------------------------
Write a python program to represent the students seeking admissing in the
university
Rules to Follows:
the details of student class are given below:
Class name:student
--Attr
             student_id
             marks
             age
Methods
(public)_init_()
       create and intialize all instance  variables to none
validate_marks()
     if data is valid, return true.Else,return false
validate_age()
    check_qualification()         validate marks and age,
if valid,check if marks is 65 or more.
  variables to set its values
getter methods include getter methods for all instance
variables to get its value
continuing with the previous scenerio,
a student eligible for admissioin has to choose a courseand pay the fees for it.
if they have scored more than85 marks in qualifing exam they get 25% discount
on fees. valid course ids and fees are given below:

course id     fees
1001          25575.0
1002          15500.0
'''
'''
class Fun():
    def __init__(self,student_id,age,marks,course_id):
        self.student_id=student_id
        self.age=age
        self.marks=marks
        self.course_id=course_id
    def valid_age(self):
        if(self.age>20):
            return True
        else:
            return False
    def valid_marks(self):
        if(self.marks>=0 and self.marks<=100):
            return True
        else:
            return False
    def check_qualification(self):
        if self.validate_marks() and self.validate_age() and self.__marks>=65:
            return True
        else:
            return False
    def eligible(self):
        if(self.marks>=85 and self.marks<=100):
            return True
        else:
            return False
    def course(self,course_id):      
            if(self.course_id==1001):
                self.fees=25575.0
            if(self.course_id==1002):
                self.fees=15500.0
            return self.fees
    def discount(self):
        if(self.eligible):
            self.fees=(25/100)*self.fees
        else:
            return self.course()
m1=Fun(1001,21,89,1001)
print(m1.course(1001))
'''


'''
class Student:
    def __init__(self,s_id,age,marks):
        self.__s_id=None
        self.__age=None
        self.__marks=None

    def validate_marks(self):
        if self.get_marks() >=0 and self.get_marks()<=100:
            return 1
        return 0

    def validate_age(self):
        if self.get_age()>20:
            return 1
        return 0

    def check_qualification(self):
        if self.validate_marks() and self.validate_age() and self.get_marks()>=65:
            print(self.fees())
            return 1
        
        return 0
      
    def fees(self):
        if self.check_qualification():
            dic={"Course 1001":25575.0,"Course 1002":15500.0}
            discount={"Course 1001":25575.0*0.75,"Course 1002":15500.0*0.75}
            print("Course List::")
            if self.get_marks()<=85:
                return (dic)
            else:
                return (discount)
        else:
            return "Not eligible for any course!"

    def set_id(self,id):
        self.__s_id=id
    def get_id(self):
        return self.__s_id

    def set_age(self,age):
        self.__age=age
    def get_age(self):
        return self.__age

    def set_marks(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks

s1=Student(0,0,0)

s1.set_id(int(input("ID:")))
s1.set_age(int(input("Age:")))
s1.set_marks(int(input("Marks:")))
print(s1.fees())
print("Qualified? :",s1.check_qualification())

'''

'''
class Fun():
    def __init__(self):
        self.__student_id=None
        self.__age=None
        self.__marks=None
    def set_id(self,id):
        self.__s_id=id
    def get_id(self):
        return self.__s_id
    def set_age(self,age):
        self.__age=age
    def get_age(self):
        return self.__age
  
    def set_marks(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks  
        
    def valid_age(self):
        if(self.__age>20):
            return True
        else:
            return False
    def valid_marks(self):
        if(self.__marks>=0 and self.__marks<=100):
            return True
        else:
            return False
    def course(self,marks):
        d={"CSE":2554,"MECh":2555}
        if(marks>85):
            for i in d:
                d[i]=d[i]-d[i]*0.25
            print("The course is offered to you after discount of 25%",d)
        else:
            print("The course offered to u:",d)
    def valid_qualification(self):
        if(self.__marks and self.valid_marks() and self.valid_age() ):
            self.course(self.__marks)
            return True
        else:
            return False

s1=Fun()
s1.set_id(9)
s1.set_age(21)
s1.set_marks(44)
if(s1.valid_qualification()):
    print("Admission can be done")
else:
    print("admission can not be done")

'''



#Que 3
#Pizza
'''
class Customer:
    def __init__(s,no) -> None:
        s.__no_of_pizza=no
    def validate_quantity(s):
        if(s.__no_of_pizza>=1 and s.__no_of_pizza<=5):
            return True
        else:
            return False
    def set_no(s,no):
        s.__no_of_pizza=no
    def get_no(s):
        return s.__no_of_pizza

class Pizzaservice:
    count = 100
    def __init__(s,type,customer,topping=False) -> None:
        s.__additional_topping=topping
        s.__size=type
        s.__cost=None
        s.__service_id=None
        s.__customer=customer
        s.calculate_cost()
    def validate_type(s):
        if(s.__size.lower() in ["small","medium"]):
            return True
        else:
            return False
    def calculate_cost(s):
        if(s.__customer.validate_quantity() and s.validate_type()):
            if(s.__size=="small"):
                if(s.__additional_topping):
                    s.__cost=180*s.__customer.get_no()
                else:
                    s.__cost=150*s.__customer.get_no()
                s.generate_service_id()
            elif(s.__size=="medium"):
                if(s.__additional_topping):
                    s.__cost=250*s.__customer.get_no()
                else:
                    s.__cost=200*s.__customer.get_no()
                s.generate_service_id()
        else:
            s.__cost=-1
    def generate_service_id(s):
        Pizzaservice.count+=1
        s.__service_id=s.__size[0]+str(int(s.count))
    def set_topping(s,topping):
        s.__additional_topping=topping
    def get_topping(s):
        return s.__additional_topping
    def set_type(s,type):
        s.__size=type
    def get_type(s):
        return s.__size
    def get_cost(s):
        return s.__cost
    def get_service_id(s):
        return s.__service_id
    def get_customer(s):
        return s.__customer
    
class Doordelivery:
    def __init__(s,distance,pizza) -> None:
        s.__distance=distance
        s.__pizza=pizza
        s.__cost=s.__pizza.get_cost()
        s.calculate_cost()
    def validate_distance(s):
        if(s.__distance>=1 and s.__distance<=10):
            return True
        else:
            return False
    def calculate_cost(s):
        # print(s.__pizza.get_cost())
        if(s.__cost>0):
            if(s.validate_distance()):
                if(s.__distance<=5):
                    s.__cost=s.__cost+(5*s.__distance)
                else:
                    s.__cost=s.__cost+((s.__distance-5)*7)+25
        else:
            s.__cost=-1
    def display(s):
        print()
        print("Service Id: ",s.__pizza.get_service_id())
        print("Number of pizza: ",s.__pizza.get_customer().get_no())
        print("Additional toppings: ",s.__pizza.get_topping())
        print("Distance: ",s.__distance)
        print("cost: ",s.__cost)

c1=Customer(1)
p1=Pizzaservice("medium",c1,True)
p1.calculate_cost()
d1=Doordelivery(10,p1)
d1.calculate_cost()
d1.display()
'''
