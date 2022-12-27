shoe = sorted(input().split())
counter = 1

for i in range(1,4):

    if shoe[i] != shoe[i-1]:
        counter += 1

print(4-counter)