a, b, c = map(int, input().split())

x = min(a,b,c)

if x == a: print(min(b,c))
elif x == b: print(min(a,c))
else: print(min(b,a))