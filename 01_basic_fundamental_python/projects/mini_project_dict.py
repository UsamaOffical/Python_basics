
person_details = {}

user_name = input("Enter a name : ")
user_age = input("Enter your age : ")
user_number = input("Enter your number : ")
user_city = input("Enter your city : ")
user_s_u = input("save | update : ")

if user_s_u == "save":
    person_details["Name"] = user_name
    person_details["Age"] = user_age
    person_details["Number"] = user_number
    person_details["City"] = user_city

elif user_s_u == "update":
    while True :

        user_name = input("Enter a name : ")
        user_age = input("Enter your age : ")
        user_number = input("Enter your number : ")
        user_city = input("Enter your city : ")
        user_s_u = input("save | update : ")

        person_details["Name"] = user_name
        person_details["Age"] = user_age
        person_details["Number"] = user_number
        person_details["City"] = user_city
        break

print(person_details)

