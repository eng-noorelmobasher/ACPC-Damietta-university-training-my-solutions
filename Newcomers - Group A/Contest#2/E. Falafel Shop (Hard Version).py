t = int(input())

for _ in range(t):
    
    x = int(input())
    a, b, c = map(int, input().split())
    b *= 2 ; c *= 5

    price = a+b+c
    price2 = price + 1

    if price >= 100:
        price = int(price -  (10/100) * price)
        
    if price2 >= 100:
        price2 = int(price2 - (10/100) * price2)
    elif price >= 90:
        price2 = price
    
    if price >= price2:
        print("YES")
    else:
        print("NO")