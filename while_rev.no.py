# rev no.
num =int(input('enter no ='))
t = 0
rnum = 0
while num > 0:
    t = num % 10
    rnum = rnum * 10 + t
    num = num//10
print(rnum)

