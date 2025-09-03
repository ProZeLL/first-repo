barisan = [4,5,8,1,3,2,9,4]
idx = 6
n = len(barisan)

if (idx > 0 and idx < n - 1 and barisan[idx] > barisan[idx - 1] and barisan[idx] > barisan[idx + 1]):
    res = True
else:
    res = False

#print(res)

i = 0
n=len(barisan)
#while i<=n-1:
    #if (i>0 and i<n-1 and barisan[i]>barisan[i-1] and barisan[i]>barisan[i+1]):
        #print(True)
    #else:
        #print(False)
    #i=i+1
    
i = 0
n=len(barisan)
#while i<=n-1:
    #if (i>0 and i<n-1 and barisan[i]>barisan[i-1] and barisan[i]>barisan[i+1]):
        #print(barisan[i])
    #i=i+1
    
digits = 15782
total=0
while digits>0:
    digit=digits%10
    total=total+digit
    digits=int(digits/10)
print(total)

a = 662
b = 414
if a<b:
    c=a
else:
    c=b
res=0
while res==0:
    if (a%c==0) and (b%c==0):
        res=c
    else:
        c=c-1
print(res)

digits = 13294393249932
res = 0
n=1
while digits>0:
    digit=digits%10
    res=(res*n)+digit
    digits=int(digits/10)
    n=10
print(res)