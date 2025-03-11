# lang = "python"
# chg = lang.replace("p","L")

# print(chg)
# for i in lang:
#     print(i)
    
# lis = ["usama","ahmed","muskan","aiman","shahab"]
# for i in lis:

#     print(len(i))

user = input("Enter a name : ")
# password  =input("You only enter a name or text and I will add this '@123' : ")
password  =input("Create a password but Your password must contain @123 : ")

if len(password) >= 8:
    if password.find("@") and password.find('123'):
        print(f"Hello {user}")
        print("Password created successfully!")
    else:{
        print("Please add @ and 123!")
    }    
else:{
    print("Password is to short")
}        