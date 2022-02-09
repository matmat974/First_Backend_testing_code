class calculator():
    num = 100

    #paramitarized constructor
    def __init__(self, a, b):
        self.firstNum = a
        self.secondNum = b


    def getData(self):
        print("hello, ")

    def add(self):
        return  self.firstNum + self.secondNum + self.num

    def sub(self):
        return self.num - self.firstNum - self.secondNum

cal = calculator(4, 2)
cal.getData()
print(cal.add())
print(cal.sub())

cal = calculator(5, 5)
print(cal.add())
print(cal.sub())

