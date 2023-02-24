t = int(input())
for _ in range(t):

    s = input()
    
    if s[:len(s)//2]*2 == s:
        print("YES")
    else:
        print("NO")