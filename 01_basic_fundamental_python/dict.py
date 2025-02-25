square = {x : x*x for x in range(1,6,1)}
# print(square)


dict_item_get = {
    "Usama" :{
        "programming_lang": ["HTML","CSS","JAVASCRIPT"],
        "language":["English","Urdu"],
        "phone" : 432432423
    },
    "muskan" :{
        "programming_lang": ["HTML","CSS","JAVASCRIPT","REACT"],
        "language":["English","Urdu"],
        "phone" : 54344354354
    }
}
for val in dict_item_get.items():
    print(val)

