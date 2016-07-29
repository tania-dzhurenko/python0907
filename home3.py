class Table:
    def __init__(self, color,count_legs, length, width, material):
        self.color = color
        self.count_legs = count_legs
        self.length = length
        self.width = width
        self.material = material
    def area (self):
        num = self.length* self.width
        return num
    def __str__(self):
        return 'Table (color:{},count_legs:{},material:{},area:{})'.format(self.color, self.count_legs, self.material, self.area())
Table1 = Table ('brown', 4, 10,12,'tree')
print (Table1.area())
print (Table1)

def sumto(n):
    if (n==1):
        return 1
    else:
        return n+sumto(n-1)
print(sumto(4))