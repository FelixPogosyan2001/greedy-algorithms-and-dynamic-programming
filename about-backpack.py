w,k = int(input()),int(input())
objects = []
res = 0

class Subject:
   def __init__(self,weight,price):
       self.weight = weight
       self.price = price
   def middle_price (self):
       return int(self.price / self.weight)


for i in range(k):
    data = [*map(int,input().split())]
    obj = Subject(data[0],data[1])
    objects.append(obj)

prices = [str(i.middle_price()) + ' ' + str(i.weight) for i in objects]

def minimum(arr):
    index = 0
    m = int(arr[index][0])
    for i in range(len(arr)):
        if int(arr[i][0]) < m :
            m = int(arr[i][0])
            index = i
    return index

def sort(arr):
    new_arr = []
    for i in range(len(arr)):
        identificator = minimum(arr)
        new_arr.append(arr.pop(identificator))
    return new_arr

prices = sort(prices)
prices.reverse()

for i in range(k):
    count = int(prices[i].split()[1])
    while (w != 0 and count != 0):
        res += int(prices[i][0])
        w -= 1
        count -= 1

print(res)