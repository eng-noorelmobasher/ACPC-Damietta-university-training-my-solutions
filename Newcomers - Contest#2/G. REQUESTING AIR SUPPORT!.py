n = int(input())
t = int(input())

for _ in range(t):

    k, c = map(int, input().split())

    if k <= n and c <= n:
        print("Roger that, Danger close!")
    else:
        print("Negative Sir")