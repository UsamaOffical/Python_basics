 
class Toyota_car:
    def __init__(self,brand,car_name,color,model):

        self.brand = brand
        self.car_name = car_name
        self.color = color
        self.model = model
      
    def start(self):
        print('Car is Starting...')

    def stop(self):
        print('Car is stop!')

    def show_car_details(self):
        print(f'Brand Name = {self.brand}\nCar Name = {self.car_name}\nCar color = {self.color}\nCar model = {self.model}')



class Lexuis(Toyota_car):

    def speciel_fea(self):
        print("Electic version")

    


lex = Lexuis("Toyota","Lexuis","White",2025)
lex.show_car_details()
lex.speciel_fea()



# fortuner = Toyota_car("Toyota","Fortuner","Black",2025)
# fortuner.show_car_details()
# fortuner.start()
# fortuner.stop()

