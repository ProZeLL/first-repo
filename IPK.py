subs=[1,2,3,4,5,6]
bobot=["B","D","D","B+","A","C+"]
sks=[4,4,4,3,3,2]
i=0
t=0
sum=0
ipk=0
while i<=len(subs)-1:
    sum = sum + sks[i]
    if bobot[i] == "A":
        t_sub = 4 * sks[i]
        t = t + t_sub
    elif bobot[i] == "A-":
        t_sub = 3.75 * sks[i]
        t = t + t_sub
    elif bobot[i] == "B+":
        t_sub = 3.33 * sks[i]
        t = t + t_sub
    elif bobot[i] == "B":
        t_sub = 3 * sks[i]
        t = t + t_sub
    elif bobot[i] == "B-":
        t_sub = 2.75 * sks[i]
        t = t + t_sub
    elif bobot[i] == "C+":
        t_sub = 2.33 * sks[i]
        t = t + t_sub
    elif bobot[i] == "C":
        t_sub = 2 * sks[i]
        t = t + t_sub
    elif bobot[i] == "D":
        t_sub = 1 * sks[i]
        t = t + t_sub
    else:
        t_sub = 0 * sks[i]
        t = t + t_sub
    i=i+1
    ipk=t/sum
print(ipk)