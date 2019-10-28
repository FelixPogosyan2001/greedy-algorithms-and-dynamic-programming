weight = int(input('Enter weight of backpack : '))
objects = []
table = []

class Subject:
    def __init__(self,weight,price):
        self.weight = weight
        self.price = price


for i in range(int(input('Enter count of subjects : '))):
    table.append([0 for i in range(weight)])
    data = list(map(int,input().split()))
    objects.append(Subject(data[0],data[1]))

for i in range(len(objects)):
    for j in range(weight):
        if i == 0 :
            table[i][j] = max(objects[i].price,table[i][j])
        else:    
           if objects[i].weight <= (j+1):
               if (j+1)-objects[i].weight > 0 : space = objects[i].price + table[i-1][j-objects[i].weight]
               else :  space = objects[i].price
               table[i][j] = max(table[i-1][j],space)
           else :
              table[i][j] = table[i-1][j]

print(table[len(table)-1][weight-1])