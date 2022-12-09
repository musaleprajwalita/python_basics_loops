'''
for i in range(1,5,1):
    for j in range(i):
        print(j, end= ' ')
    print()
for i in range(3,0,-1):
    for j in range(i):
        print(j , end= ' ')
    print()
'''

'''
for i in range(10):
    for j in range(i+1):
        print(j+1 ,end= ' ') # if i+1 then prints vertically
    print()
'''
n = int(input('enter no of rows'))
for i in range(n):
    for j in range(n-i-1):  #thsis added to add space at start
        print(' ', end=' ')
    for j in range(i,-1,-1):
        print(j+1, end= ' ')
    print()

