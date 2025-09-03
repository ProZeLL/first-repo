test=[31,-41,59,26,-53,58,97,-93,-23,84]
test=[-8,-9,-10,1,-11,-12,-13,-15]
ARR=[31,-41,59,26,-53,58,97,-93,-23,84]
max=-10000
i=0
while i<=len(ARR)-1:
    j=i
    total=0
    while j<=len(ARR)-1:
        total=total+ARR[j]
        if max<total:
            max=total
        j+=1
    i+=1
print(max)  
