'''
n = int(input('enter no of rows'))
for i in range(n):
    for j in range(i,-1,-1):
        print(n-j, end= ' ')
    print()
   '''
n = int(input('enter no of rows'))
for i in range(n):
    for j in range(n-i-1):  #thsis added to add space at start
        print(' ', end=' ')
    for j in range(i,-1,-1):
        print(n-j, end= ' ')
    print()

''' for every prgrm we can add space at start like above'''
