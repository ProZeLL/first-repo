digit_10 = 1716703440
digit = 10
N = 0
n = 1
while digit >= 1:
    digits = digit_10 % 10
    N = N + (n*digits)
    digit_10 = int(digit_10/10)
    n = n + 1
    digit = digit - 1
print(N)
if N % 11 == 0:
    print(True)
else:
    print(False)
    
digit_13 = 9780716703440
digit = 13
N = 0
while digit >= 1:
    if digit%2==1:
        digits = digit_13 % 10
        N = N + (1*digits)
        digit_13 = int(digit_13/10)
        digit = digit - 1
    else:
        digits = digit_13 % 10
        N = N + (3*digits)
        digit_13 = int(digit_13/10)
        digit = digit - 1
print(N)
if N % 10 == 0:
    print(True)
else:
    print(False)