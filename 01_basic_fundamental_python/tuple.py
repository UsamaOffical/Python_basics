tup = (1,2,4,5,"usama",True)

tup_2 = ()
# print(type(tup_2))

tup_3 = (1,3,4,6,7)
# print(tup_3[0:3:1])

# user_name_pass :list[tuple[str,str]] = [('Usama','123'),('ahmed','456'),('awais','789'),('shoaib','1011')] 
# # user_name = [['usama',123],['ahmed',456],['shoaib','awais']]
# user = input('Enter your name : ')
# passw = input('Enter your password : ')

# for name_pass in user_name_pass:
#     name , password = name_pass # zip
#     if user != name and passw != password:
#         print(f'welcome {user}')
#         break
#     print(name,password)


usr_inp = int(input('Enter a number that You crete a table! '))

for n in range(1,11):
    print(f'{usr_inp} x {n} = {usr_inp*n}')

print(type(usr_inp))


