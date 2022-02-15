# from faker import Faker

#
# fake = Faker()
# aisle = fake.isbn10()


def addBook(isbn, aisle):
    body = {
        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": aisle,  # aisle is being parametarized so it can be easily changed
        "author": "Johny foe"
    }
    return body


def deleteBook(bookID):
    body = {
        "ID": bookID  # id is also being a parametarized
    }
    return body
