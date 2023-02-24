n = int(input())

distance = list(map(int, input().split()))
skill = list(map(int, input().split()))

#we will sort both distance and skill so the smallest skill can get the smallest distance and so on.

distance.sort()
skill.sort()

check = True
for i in range(n):
    #we will check if the little bird will score or not :) .
    if skill[i] < distance[i]:
        check = False
        break

if check:
    print("YES")
else:
    print("NO")