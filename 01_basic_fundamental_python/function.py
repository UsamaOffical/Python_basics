def greet(name="Usama",age=18):
    print(f"Hello {name} your age is {age}")

# greet("Usama jameel",23)


# -----------------   Decorator
# def my_decorator(func):
#     def wrapper():
#         print("Something before happing when the function is called!")
#         print("Something after happing when the function is called!")
#         func()
#     return wrapper    
    
# @my_decorator
# def hello_func():
#     usr = input("enter name!")
#     print(f"Hello {usr}")
# hello_func()

# -----------------   Generator

# def count_num(num):
#     while num > 0:
#         yield num
#         num -= 1

# for nums in count_num(11):
#     print(nums)

# ----------------  lamda

lamd = lambda exp:exp*int(input("enter a number : "))
# print(lamd(2))
 



class Charactor:
    def __init__(self,name,health,attack):
        self.name = name
        self.health = health
        self.attack = attack
        
    def enemy_attack(self):
        print(f"Name {self.name} health {self.health} attack power {self.attack}")

worrior = Charactor("Thor",100,90)    
mage = Charactor("mage",67,40)    
gandalf = Charactor("gandalf",85,75)    


char_1 = input("Thor | mage | gandalf : ")
char_2 = input("Thor | mage | gandalf : ")

if char_1 == "Thor" and char_2 == "mage":
    if worrior.attack > mage.attack and worrior.health > mage.health:
        print(f"{worrior.name} win!") 
    elif worrior.attack < mage.attack and worrior.health < mage.health:
        print(f"{mage.name} win")       
         
     