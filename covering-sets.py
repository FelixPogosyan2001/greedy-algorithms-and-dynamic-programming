states_needed = set(input('Enter all states: ').split(' '))
count = int(input('Count of the stations - '))
stations = {}
result = set()

for i in range(count):
    key = input('Enter a station: ')
    value = set(input('Enter states for this station: ').split(' '))
    stations[key] = value


while states_needed: #O(n)
    best_station = None #O(1)
    states_covered = set() #O(1)
    for station,state_for_station in stations.items(): #O(n)
        covered = state_for_station & states_needed #O(1)
        if len(covered) > len(states_covered): #O(1)
            best_station = station #O(1)
            states_covered = covered #O(1)
    states_needed -= states_covered #O(1)
    result.add(best_station) #O(1)
#0(n*n) + O(1*8) = O(n^2) 
print(result)