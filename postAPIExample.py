import json
import configparser
from payLoad import *
from utilities.configaration import *
from utilities.resources import *
from utilities.authentication import *

import requests


#it store the endpoint as a global variable and optimize the code

# header = {"Content-Type" : "application/json"}
# addBookUrl = getConfig()['API']['endpoint']+apiResources.addBook
# deleteBookUrl = getConfig()['API']['endpoint']+'/Library/DeleteBook.php'
#
#
# add_bookresponse = requests.post(addBookUrl, json=addBook("0001"), headers=header)
#
#
#
# print(add_bookresponse.json())
# #print(add_bookresponse.headers)
# response_json = add_bookresponse.json()
# print(type(response_json))
# # print(response_json['ID'])
# bookID = response_json['ID']
# print(bookID)
# #delete book
# delete_book = requests.post(deleteBookUrl,json=deleteBook(bookID), headers=header,)
#
#
# assert delete_book.status_code == 200
# resjson = delete_book.json()
# print(resjson["msg"])
# assert resjson["msg"] == "book is successfully deleted"



#Authentication

hello = requests.session()
hello.auth = auth = ('matmat974', authe.token)
url = 'https://api.github.com/user'

github_response = hello.get(url)
print(github_response.status_code)
#
# url1 = 'https://api.github.com/user/repos'
#
# response = hello.get(url1)
# print(response.status_code)