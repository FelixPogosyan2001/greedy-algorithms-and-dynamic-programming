query = 'blue'
values = {'clues':0}

for value in values.keys():
    table = []
    maxim = 0
    for i in range(len(query)):
        table.append([0 for i in range(len(value))])
        for j in range(len(value)):
            if query[i] == value[j] and j==0:
                table[i][j] = 1
            elif query[i] == value[j] and j!=0 and i!=0:
                table[i][j] = table[i-1][j-1] + 1
    for line in table:
        if maxim < max(line): maxim = max(line)
    values[value] = maxim
        

print(values) 