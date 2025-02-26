

class Charactor:
    def __init__(self,name,health,attack):
        self.name = name
        self.health = health
        self.attack = attack
        
    def enemy_attack(self):
        print(f"Name {self.name} health {self.health} attack power {self.attack}")

worrior = Charactor("thor",100,90)    
mage = Charactor("mage",67,40)    

char_1 = input("thor | mage | gandalf : ")
char_2 = input("thor | mage | gandalf : ")

if char_1 == "thor" and char_2 == "mage":
    if worrior.attack > mage.attack and worrior.health > mage.health:
        print(f"{worrior.name} win!") 
    elif worrior.attack < mage.attack and worrior.health < mage.health:
        print(f"{mage.name} win")     


