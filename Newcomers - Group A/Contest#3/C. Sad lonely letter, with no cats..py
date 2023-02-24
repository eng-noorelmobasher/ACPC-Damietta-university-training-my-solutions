for _ in range(int(input())):

    s = input()
    c = input()

    for i in range(0,len(s),2):

        if s[i] == c:
            print("YES")
            break
        
    else:
        print("NO")