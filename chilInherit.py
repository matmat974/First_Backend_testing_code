from oopTutorial import calculator


class childInherit(calculator):
    num2 = 200

    def __init__(self):
        calculator.__init__(self, 10, 2)

    def getDataCompleted(self):
        return self.num2 + self.num + self.add()


child = childInherit()
print(child.getDataCompleted())