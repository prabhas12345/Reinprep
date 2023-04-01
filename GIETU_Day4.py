#Que 1
'''Write a python function,nearest_palindrome() which accepts a number and
returns the nearest palindrome greater than the given number.

      Sample Input             Output
            99                  101
           1221                1331
num = 1221
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")
    
def nearest_palindrome():
    large=temp
    while large>temp'''

'''
import sys
def next_smallest_Palindrome(num):
    for i in range(num+1,sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i
print(next_smallest_Palindrome(99))
print(next_smallest_Palindrome(1221))
'''

#Que 2
#Care Hospital

'''
Care hospital want to know the medical speciality visited by the ma no.of patients.assume that the patient id
of the patient along with the medical speciality visited by the patient is stored in a list.
The details of the medical specialities are stored in dictionary as follows:
{"p":"pediatrics","o":"orthopedics","E":"ENT"}
write a fun to find the medical speciality visisted by the max no.of patients and return the name of the speciality. 
Note 1: Assume that there is always only one medical speciality which is visited
by maximun number of patients and return the name of the speciality.
Note 2: 
Perform case sensitivite string comparasion wherever necessary.

    Sample Input                              Expected Output
[101,P,102,O,302,P,305,P]                        Pediatrics
[101,P,102,O,302,P,305,E,401,0,656,O]            Orthopedics
[101,P,102,O,302,P,305,P,401,E,656,O,987,E]      ENT
'''

'''
def max_visited(pm_spl_list,med_spl):
    max_visit=0
    P = pm_spl_list.count('P')
    E = pm_spl_list.count('E')
    O = pm_spl_list.count('O')
    if P>E and P>0:
        spl = med_spl['P']
    elif E>0:
        spl = med_spl['E']
    else:
        spl = med_spl['O']
    return spl
pm_spl_list = [301,'P',302,'P',305,'P',401,'E',656,'E']
med_spl = {'P':'Pediatrics','O':'Orthopedics','E':'ENT'}
spl = max_visited(pm_spl_list,med_spl)
print(spl)
'''

#Que 3
'''Write a python function to display all the commom characters btw two strings.
Return -1 if there are no matching characters.
Note:ignore blank spaces if there are any.
perform case sensitivity string comparision whenever necessary.

Sample input:                                  Output:
"I like python"                         
"java is a very popular language"              lieyon
'''

'''
def match(str1,str2):
    str1 = str1.replace(" "," ")
    str2 = str2.replace(" "," ")
    common = ""
    for char in str1:
        if char in str2 and char not in common:
            common += char
    if len(common) > 0:
        return common
    else:
        return -1
str1 = str("I like python")
str2 = str("java is a very popular language")
result = match(str1,str2)
print(result)
'''

# oops with Python
#Snippet 1

'''
class Example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
'''
#Snippet 2
'''
class Example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
'''

#Snippet 3
'''
class Customer:
    def _init_(self):
        self.cust_id = 100
c1=Customer()
print(c1.cust_id)
'''

#Snippet 4
'''
class Customer:
    def _init_(self,id):
        self.id = 100
c1=Customer(200)
print(c1.id)
'''

#Snippet 5
'''
class Shoe:
	def __init__(self,price,material):
		self.price=price
		self.material=material
s1=Shoe(100,"Canvas")
print(s1.price,s1.material)
'''

#Snippet 6
'''
class Shoe:
	def __init__(self,price,material):
		self.price=price
		self.material=material
s1=Shoe(100,"Canvas")
print("The unique id of the object",id(s1))
'''

#Snippet 7
'''
class Shoe:
    def __init__(self,price,material):
        self.price = price
        self.material = material
    def __str__(self):
        return "shoe with price:" +str(self.price)+"and material:"+self.material
s1=Shoe(1000, "Canvas")
print(s1)
'''
#Snippet 8
'''
class Mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("Displaying details")
    def purchase(self):
        self.display()
        print("calculating price")
Mobile().purchase()
Mobile().purchase()
m1=Mobile()
print(m1)
m2=Mobile()
print(m2)
m1=m2
print(m1)
print(m2)
'''

#Snippet 9
'''
class Mobile:
	def __init__(self,brand,price):
		self.brand=brand
		self.price=price
		self.total_price=None
	def purchase(self):
		if self.brand=="apple":
			discount=10
		else:
			discount=5
		self.total_price=self.price-self.price*(discount/100)
		print("Total price of",self.brand,"Mobile is",self.total_price)
mob1=Mobile("Apple",20000)
mob2=Mobile("Moto",15000)
mob1.purchase()
mob2.purchase()
#print(mob1.amount_returned())
#print(mob2.amount_returned())
'''

#Snippet 10
'''
class Customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id =cust_id
        self.name = name
        self.age=  age
        self.wallet_balance=wallet_balance
    def update_balance(self,amount):
       if amount<1000 and amount >0:
           self.wallet_balance+=amount
    def show_balance(self):
        print("The Balance is",self.wallet_balance)
c1=Customer(100,"Litu",24,1000)
c1.show_balance()
'''

#Snippet 11
'''
class Customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance
    def set_balance(self,amount):
        if amount < 50000 and amount > 0:
            self.__wallet_balance += amount
    #def show_balance(self):
            #print("The balance is",self.__wallet_balance)
    def get_wallet_balance(self):
        return self.__wallet_balance
c1=Customer(100,"Litu",25,1000)
print(c1.get_wallet
c1.get_wallet_balance
#print(c1._wallet_balance)..._wallet_balance gives error 
c1.set_balance(5000)
print(c1.get_wallet_balance())
'''

#Snippet 12
'''
class Dam:
    def __init__(self,name,length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length
dam1=Dam("ABC dam",3.5)
print("Dam name:",dam1.name)
print("Dam Length",dam1.get_length())
'''

#Snippet 13
'''
class Table:
    def _init_(self):
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None
    def assign_data(self,glass_top,wooden_top):
        self.__glass_top=glass_top
        self.__wooden_top=wooden_top
    def identify_rate(self,glass_top,wooden_top):
        self.assign_data(glass_top,wooden_top)
        if(self.__glass_top==True):
            rate=20000
        elif(self.__wooden_top==True):
            rate=30000
print(
'''

#Snippet 14
'''
class Table:
	def __init__(self):
		self.no_of_legs=4
		self.glass_top=None
		self.wooden_top=None
dining_table=Table()
back_table=Table()
front_table=back_table
back_table=dining_table
print(id(dining_table),id(back_table),id(front_table))
'''









