#print numbers from 1 to n in any order.
t = int(input())

for i in range(t):

    n = int(input())
    for j in range(1,n+1):
        print(j,end=" ")
    print()