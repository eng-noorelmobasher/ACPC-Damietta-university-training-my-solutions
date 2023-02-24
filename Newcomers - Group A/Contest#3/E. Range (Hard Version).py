t = int(input())

for _ in range(t):

    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    print(max(numbers) - min(numbers))