# su of digits
'''
num = int(input('enter no.'))
r = 0
s = 0
while (num != 0):
    r = num % 10
    s = s + r
    num = num // 10
print('sum of digits are = ', s)
'''

# product of digits
num = int(input('enter no.'))
r = 0
p = 1
while (num != 0):
    r = num % 10
    p = p * r
    num = num // 10
print('sum of digits are = ', p)



