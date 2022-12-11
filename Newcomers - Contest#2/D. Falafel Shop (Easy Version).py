t = int(input())

for _ in range(t):
    
    x = int(input())
    a, b, c = map(int, input().split())
    b *= 2 ; c *= 5

    price = a+b+c

    #now we check if the number is greater than or equal to 100
    if price >= 100:
        price = int(price - price*10/100)
    
    #now we check if the price is less than or equal to x or not
    if price <= x:
        print("YES")
    else:
        print("NO")