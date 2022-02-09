from behave import *
from payLoad import *
from utilities.configaration import *
from utilities.resources import *
from utilities.authentication import *



import requests


@given('the book which needs to be added to library')
def step_impl(context):
    context.header = {"Content-Type": "application/json"}
    context.addBookUrl = getConfig()['API']['endpoint'] + apiResources.addBook
    context.payLoad = addBook('bookID', '0009')




@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.addBookUrl, json=context.payLoad, headers=context.header)




@then('book is succesfully added')
def step_impl(context):
    print(context.response.json())
    # print(add_bookresponse.headers)
    context.response_json = context.response.json()
    print(type(context.response_json))
    # print(response_json['ID'])
    context.bookId = context.response_json['ID']
    print(context.bookId)

    assert context.response_json['Msg'] == "successfully added"

@given('the book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.header = {"Content-Type": "application/json"}
    context.addBookUrl = getConfig()['API']['endpoint'] + apiResources.addBook
    context.payLoad = addBook(isbn, aisle)



@given('I have github auth credentials')
def step_impl(context):
    context.hello = requests.session()
    context.hello.auth = auth = ('matmat974', authe.token)



@when('I hit getRepo API of github')
def step_impl(context):
    context.response = context.hello.get(apiResources.gitHubRepo)



@then('status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.response.status_code)

    assert context.response.status_code == statusCode