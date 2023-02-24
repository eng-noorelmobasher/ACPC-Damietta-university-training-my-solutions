x, y = map(int, input().split())

maximum = [x-y, x*y, x//y]

print(max(maximum))