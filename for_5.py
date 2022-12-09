'''
n = int(input('enter no of rows'))
for i in range(n):
    for j in range(i+1):
        print(n-i, end= ' ')
    print()
'''

n = int(input('enter no of rows'))
for i in range(n):
    for j in range(i+1):
        print(n-j, end= ' ')
    print()
