k = int(input())
nums = list(map(int,input().split()))
sorted_nums = sorted(nums)
table = []
shift = 0 
l = 0

for i in range(k) : sorted_nums[i] = nums.index(sorted_nums[i])

for i in range(k):
    table.append([0 for i in range(k)])
    shift = 0
    for j in range(k):
        if sorted_nums[i] == sorted_nums[j] : table[i][j] += 1
        elif sorted_nums[i+shift] < sorted_nums[j] and i <= j: 
            table[i][j] = table[i][j-1] + 1
            shift = j - i
        else : table[i][j] = table[i][j-1]

for row in table:
    if row[k-1] > l : l = row[k-1]
    
print(l)