n = 37465828
total = 0
while n != 0:
    digit = n % 10
    if digit % 2 == 0:
        total = total + digit
        n = int(n/10)
    else:
        n = int(n/10)
print(total)