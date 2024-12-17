n = 5
ch = 0

for x in range(0,n):
    p1 = x
    for y in range(1,n+1):
        x += n
        print(chr(x-n+65)+"",end=" ")
    print()
