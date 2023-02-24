n = int(input())

monsters_health = list(map(int, input().split()))

monsters_health.sort()

counter = 1
for i in range(1,n):
    if monsters_health[i] != monsters_health[i-1]:
        counter += 1

print(counter)