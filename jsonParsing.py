import json


# courses = '{"name": "Rahul Shetty", "language": ["java", "python"]}'

#loads methon parse Json and it returns dictionary

# dict_courses = json.loads(courses)
#
# print(type(dict_courses)) #validate if dict_courses is already a dictionary
# print(dict_courses)
# print(dict_courses['name']) #print name in json
# list_language = (dict_courses['language']) #convert language json into a dictionary
# #convert the json data language into own dictionary variable
# print(type(list_language)) #validate if list_language is dictionary
# print(list_language[0]) #print list_language dictionary
#
# #single line method to print language that are dictionary
# print(dict_courses['language'][1])

# with open('/Users/matthew/Downloads/sample2.json') as f:
#     data = json.load(f)

    # print(type(data))
    # # print(data)
    # # print(data['firstName'])
    # # print(data['lastName'])
    # print(data['phoneNumbers'][0]['number'])
    # print(data['address']['city'])
    #
    #
    # print(type(data['address']))
    # print(type(data['phoneNumbers']))

with open('/Users/matthew/Downloads/jsonpractice5.json') as a:
    storage = json.load(a)

    # print(type(storage['courses'][1]['details']))
    print(storage['courses'][1]['details']['site1'][1])
    # print(storage['courses'][1]['details']['site'][1])
    # for website in storage['courses'][1]['details']['site']:
    #     print(website)
    # for courses in storage['courses']:
    #     # print(courses)
    #
    #     # if(courses['title'] == 'Selenium Python'):
    #     #     print("The price of ", courses['title'], " is ", courses['price'], " and it have ", courses['copies'], " copies ", "it also have two website one is  ", courses['details']['site'], " and the other one is ", courses['details']['site1'])
    #     if(courses['title'] == 'Cypress'):
    #         print("The price of ", courses['title'],  " is ", courses['price'], " and it have ", courses['copies'], " copies")
    #         # print(courses['price'])
    #         assert courses['price'] == 40

#
# with open('/Users/matthew/Downloads/jsonpractice4.json') as b:
#     storage1 = json.load(b)
# compare two json file
#     print(storage == storage1)
