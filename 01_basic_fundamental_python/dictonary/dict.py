# # square = {x : x*x for x in range(1,6,1)}
# # # print(square)


# # dict_item_get = {
# #     "Usama" :{
# #         "programming_lang": ["HTML","CSS","JAVASCRIPT"],
# #         "language":["English","Urdu"],
# #         "phone" : 432432423
# #     },
# #     "muskan" :{
# #         "programming_lang": ["HTML","CSS","JAVASCRIPT","REACT"],
# #         "language":["English","Urdu"],
# #         "phone" : 54344354354
# #     }
# # }
# # for val in dict_item_get.items():
# #     print(val)

# # from typing import Dist

# # world_city= {
# #     'Pakistan':'Karachi',
# #     'Suadia':'Riyadh',
# #     'India':'Mombie',
# #     'Bangladesh':'Dhaka',
# #     'America':{
# #         'Los Anelos':'los amara',
# #         'Los marina':'claiba',
# #         'washingTon':'Sans california',
# #     }
# # }
# # world_city['Canada'] = 'Lahore'
# # world_city.update({"lanada":"Islamabad"})
# # val = world_city.items()

# # # for i in world_city:
# # #     print(i, world_city[i])

# # for key,vals in val: # zip
    
    
# #     print(f'{key.upper()} --> {vals}')
# # # print(val)

# usr_id = input("Enter your id : ")
# usr_name = input("Enter your name : ")
# usr_age = input("Enter your age : ")
# usr_phone = input("Enter your phone : ")

# keys = ['id','name','age','phone']

# data = {}
# data = data.fromkeys(keys)
# # data['id'] = usr_id
# # data['name'] = usr_name
# # data['age'] = usr_age
# # data['phone'] = usr_phone
# data.update({'id':usr_id})
# data.update({'name':usr_name})
# data.update({'age':usr_age})
# data.update({'phone':usr_phone})

# print(data)

# dic = {'id_1':123,'id_2':223,'id_3':456}

# key_value = dic.items()

# values = { k:v for k,v in key_value }
# # print(values) # shuffle

# for i in values:
#     print(i ,values[i]) # sorted

