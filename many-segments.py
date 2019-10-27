n,k = map(int,input().split(' '))
res = 0
deleted = []
used = []
lines = []
nums = {}
bed_nums = {}

for i in range(n): #O(n)
    lines.append(input())

for item in lines: #O(n^2)
    a,b = map(int,item.split(' '))
    for num in range(a,b+1):
        if (not str(num) in nums):
            nums[str(num)] = 1
        else :
            nums[str(num)] += 1

for key,value in nums.items(): #O(n)
    if value > k :
        bed_nums[key] = value - k

while bed_nums: #O(n) * O(n^2) * O(n) = O(n^4)
    count = 0
    best_line = None
    identificate = -1
    for ID in range(len(lines)): #O(n^2)
        a,b = map(int,lines[ID].split(' '))
        q = 0
        for key,value in bed_nums.items():
            if int(key) >= a and int(key) <= b:
                q += 1
        if q > count and not (ID in used):
            count = q
            best_line = lines[ID]
            identificate = ID
    used.append(identificate)
    l,r = [*map(int,best_line.split(' '))]
    for i in range(l,r+1): #O(n)
        if str(i) in bed_nums : 
            bed_nums[str(i)] -= 1
            if bed_nums[str(i)] == 0: del bed_nums[str(i)]

    deleted.append(identificate + 1)
    res += 1
    
print(res)
print(' '.join([*map(str,deleted)]))

#O(n^4) + O(2n) + O(n^2) = O(n^4)