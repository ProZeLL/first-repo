import sys
arrival_time = [0,1,3,4,6,7]
service_time = [3,5,2,4,3,3]
start_time = [0,0,0,0,0,0]
smallest = sys.maxsize
search_start_time = 0
batas = 0
for i in range(len(service_time) - 1):
    
    for j in range(len(arrival_time)):
        if arrival_time[j] <= search_start_time:
            if service_time[j] <= smallest:
                smallest = service_time[j]
                idx = j
    start_time[idx] = arrival_time[i+1] + service_time[idx]
    search_start_time = search_start_time + arrival_time[idx]
    service_time[idx] = sys.maxsize
print(start_time)
        