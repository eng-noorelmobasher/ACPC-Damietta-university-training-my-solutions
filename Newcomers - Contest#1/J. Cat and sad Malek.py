n, k = map(int, input().split())

"""
firstly:
1 * 5 = 5
2 * 5 = 10
3 * 5 = 15
4 * 5 = 20
5 * 5 = 25
5 * 6 = 30

we will notice that if k is even then the last digit will be 0 but if k is odd then the last
digit will be 5.

and
if 5 rasied to any power the last digit will not change.
"""
if k % 2 == 0:
    print(0)
else:
    print(5)