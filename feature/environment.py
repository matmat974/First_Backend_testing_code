import requests
from utilities.configaration import *
from utilities.resources import *


def after_scenario(context, scenario):
    if "library" in scenario.tags:
        deleteBookUrl = getConfig()['API']['endpoint'] + '/Library/DeleteBook.php'
        context.header = {"Content-Type": "application/json"}

        delete_book = requests.post(deleteBookUrl, json={'ID' : context.bookId}, headers=context.header)

        assert delete_book.status_code == 200
        resjson = delete_book.json()
        print(resjson["msg"])
        assert resjson["msg"] == "book is successfully deleted"

