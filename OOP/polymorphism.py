
class Bird():
    def sound(self):
        print("Birds sounds 'chiu chiu'")
    def name(self):
        print("this is bird class")

class Crow(Bird):
    def sound(self):
        print("Crow sounds 'Caw caw'")

class Parrot(Bird):
    def sound(self):
        print("Parrot sounds 'Tae tae'")

bird_1 = Crow()
bird_1.sound()
bird_1.name()

# polymorphism is taraha se kam karta hai k agr ek class mai dusri class pass ki jae us k parameter mai or agr dono class mai ek jesa method ho jo ek hi nam se ho to ot hum child class mai .method pas kare gae to humare pas child class k andar jo method hoga wo override kar jae ga parent class k method ko