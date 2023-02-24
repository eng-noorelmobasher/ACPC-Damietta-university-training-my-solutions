n = int(input())
s1 = ""

for i in range(n):
    s1 += ''.join(input().split())

m = int(input())
s2 = ""

for i in range(m):
    s2 += ''.join(input().split())

if s1 == s2:
    print("YES")
else:
    print("NO")