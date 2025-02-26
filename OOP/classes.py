class Student:
    def set_details(self,name,age,roll_num):

        self.name = name
        self.age = age
        self.roll_num = roll_num

    def Show_details(self):
        print(f'Student Name : {self.name}\nStudent Age : {self.age}\nStudent Roll-num : {self.roll_num}')

std_1 = Student()
std_1.set_details("Usama",24,337638)
std_1.Show_details()

std_2 = Student()
std_2.set_details("Muskan",22,337345)
std_2.Show_details()

std_3 = Student()
std_3.set_details("Ahmed",28,357662)
std_3.Show_details()

std_4 = Student()
std_4.set_details("Aiman",24,337635)
std_4.Show_details()

print(type(std_1))