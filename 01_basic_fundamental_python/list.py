lis = list((1,2,57,"usama",True,23.4))
# print(lis)

lis[0:3] = "ahmed","shoaib","muskan" # change element use slicing
# print(lis)
# print(lis * 3) # repeat 3 time 

# ---------------------- check in the list 
# check_in = [1,2,3,4,5,6,78,8,99]
# check = int(input("Enter a number to check in list : "))

# if check in check_in:
#     print("Yes found")
# else:
#     print("Not found!")
     

# check_not_in = [1,2,3,4,5,6,78,8,99]

# check_not = int(input("Enter a number to check in list : "))

# if check_not not in check_not_in:
#     print("Yes not found")
# else:
#     print("yes found!")


lst = [1,2,34,5,6]
lst_2 = lst.copy()
lst_2[3] = "usama"
# print(lst_2,lst)

# ------------------- list method 
#--------append add element in last
lst_3 = [12,23,4]
lst_3.append(4)
# print(lst_3)

#--------extend merge to list
lst_4 = [12,23,4]
lst_4.extend(lst)
# print(lst_4)

#-------- pop remove the element that index you pass in 
lst_4 = [12,23,4]
lst_4 = [12,23,4]
# print(lst_4.pop(0))


#-------- remove method remove the element that you pass in 
lst_4 = [12,23,4]
# print(lst_4.remove(12))


#-------- clear is clear list
lst_4 = [12,23,4]
# print(lst_4.clear())

# ------------- convert list to set then check two same element 
ls_1 = [1,23,4]
ls_2 = [1,25,4]

s1 = set(ls_1)
s2 = set(ls_2)

s3 = s1.intersection(s2)
print(s3)



