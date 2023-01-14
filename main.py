from mongoengine import *
from datetime import datetime
import os
import json
import time
connect("aadhar_dev_2")
class User(Document):
    username = StringField(required=True)
    age=IntField()
    aadhar_num=LongField(min_value=000000000000, max_value=999999999999)
    address=StringField(max_length=200)
    #dob=DateTimeField()
    def json(self):
        user_dict = {
            "username":self.username,
            "age":self.age,
            "aadhar_num":self.aadhar_num,
            "address":self.address
        }
        return json.dumps(user_dict)
    # meta = {
    #     "indexes":  ["aadhar_num", "username"],

    # }


## saving documents 
user = User(
    username="Modi",
    age="32",
    aadhar_num= 123088787210,
    address="Barasirsohi, Qatar, 208016"
).save()

user1 = User(
    username="Messi",
    age="32",
    aadhar_num= 113476786969,
    address="Barasirsohi, haveli, 208016"
)
user1.save()
##keep this running inside an infinite loop of the sleep kind and then it is ready for deploying 
# n = int(input("Enter the 12 digit aadhar number : "))
# ## take aadhar number input
# ## if it exists, output
# ## else just enter it into the database 
# user2=User(
#     username="trial entry",
#     age="99",
#     aadhar_num=n,
#     address="dhjrvfbrehjfer"
# )
# # john_doe=User.objects(aadhar_num=n).get()
# # print(john_doe.json())
# try:
#     john_doe=User.objects(aadhar_num=n).get()
#     print("User with same aadhar already exists as:  ")
#     print(john_doe.json())
# except DoesNotExist:
#     user2.save()
#     print("Entered record of new user")
#     user3=User.objects(aadhar_num=n).get()
#     print(user3.json())
#     # user2=User.objects(aadhar_num=n).get()
#     # print(json(user2))

# print("Done..start again for new user query")
while True:
    n = int(input("Enter the 12 digit aadhar number : "))
    user2=User(username="trial entry",age="99",aadhar_num=n,address="dhjrvfbrehjfer")
    try:
        john_doe=User.objects(aadhar_num=n).get()
        print("User with same aadhar already exists as:  ")
        print(john_doe.json())
    except DoesNotExist:
        user2.save()
        print("Entered record of new user")
        user3=User.objects(aadhar_num=n).get()
        print(user3.json())
    print("Done..start again for new user query")






