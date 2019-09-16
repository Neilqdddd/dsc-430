'''
Yili Lin
2/19/2019
I have not given or received any unauthorized assistance on this assignment.
'''
import random

class SixSidedDie():
    'class of six side dice'
    def __init__(self,x=0):
        'values of instance members'
        self.x=x

    def roll(self):
        'function of roll dice'
        self.x = random.randrange(1, 7)
        return self.x

    def getFaceValue(self):
        'return the value of the dice'
        return self.x

    def __repr__(self):
        'string present the dice face'
        return f'SixSidedDie({self.x})'

class TenSidedDie(SixSidedDie):
    'class of ten side dice'

    def roll(self):
        'function of roll dice'
        self.x = random.randrange(1, 11)
        return self.x

    def __repr__(self):
        'string present the dice face'
        return f'TenSidedDie({self.x})'

class TwentySidedDie(SixSidedDie):
    'class of 20 side dice'

    def roll(self):
        'function of roll dice'
        self.x = random.randrange(1, 21)
        return self.x

    def __repr__(self):
        'string present the dice face'
        return f'TwentySidedDie({self.x})'

class Cup():
    'class cup of hold the 6,10,20 dice'

    list_count = []
    sum = 0
    def __init__(self, sixside=1, tenside=1, twentyside=1):
        'values of instance members'
        self.six = sixside
        self.ten = tenside
        self.twenty = twentyside

    def rollone(self,num,classname):
        'roll one dice'
        for i in range(0,num):
            self.name=classname
            self.name.roll()
            self.list_count.append(self.name)
            self.sum+=classname.getFaceValue()

    def roll(self):
        'roll all dice'
        self.rollone(self.six,SixSidedDie())
        self.rollone(self.ten,TenSidedDie())
        self.rollone(self.twenty,TwentySidedDie())
        return self.sum

    def getSum(self):
        'sum'
        return self.sum

    def __repr__(self):
        'string the value of each dice'
        return (f'Cup({str(self.list_count)[1:-1]})')






