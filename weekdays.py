import datetime

weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


class WeekStruct():
    def __init__(self):
        pass

    def weekday(self):
        for name in weekdays:
            name.sort(reverse=True)
            return name

    def year(self):
        y = datetime.date.today().year
        return y

    def numberlist():
        numlist = numbers.sort()
        print numlist

    def printtest(self):
        i = 1
        while i < 10000:
            print "Hello World", i
            i = i + 1

class Sorter():
    def __init__(self):
        pass
    def numbersorter(self):
        numbers = ['2', '1', '4', '7', '6', '5', '3']
        numbers.sort()
        return numbers

s = Sorter()
print s.numbersorter()