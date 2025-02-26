
# class Student:
#     def __init__(self,name,age,roll_num):

#         self.name = name
#         self.age = age
#         self.roll_num = roll_num

#     def Show_student_detail(self):
#         print(f'Student Name : {self.name}\nStudent Age : {self.age}\nStudent Roll-num : {self.roll_num}')
    
#     def greet(self):
#         print(f'Welcome to GIAIC {self.name}!')

# std_1 = Student("Usama",23,33435)
# std_1.Show_student_detail()
# std_1.greet()


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


fortuner = Toyota_car("Toyota","Fortuner","Black",2025)
fortuner.show_car_details()
fortuner.start()
fortuner.stop()
