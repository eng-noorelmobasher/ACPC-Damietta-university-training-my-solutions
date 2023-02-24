t = int(input())
for _ in range(t):

    n = int(input())
    #if the polygon has 3 sides then the sum of angles is 180 and when we add 1 side the sum increases to 360!
    #so we can see that (n-2)*180 would be the solution
    print((n-2)*180)