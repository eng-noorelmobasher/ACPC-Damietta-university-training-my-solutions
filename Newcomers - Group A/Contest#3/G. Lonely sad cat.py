t = int(input())

for _ in range(t):

    n = int(input())
    cats_id = list(map(int, input().split()))

    mn = min(cats_id)
    mx = max(cats_id)

    if cats_id.count(mx) > 1:
        print(cats_id.index(mn)+1)
    else:
        print(cats_id.index(mx)+1)