t = int(input())

for _ in range(t):

    n, k = map(int, input().split())

    total_available_products = []

    for i in range(n):
        shop_products = list(map(int, input().split()))
        #Buying at most 2 products from each shop, we will take the first cheap two!
        shop_products.sort()
        total_available_products += shop_products[:2]

    #sort the total list to get the cost of the products in an ascending order
    total_available_products.sort()
    
    counter = 0
    for i in range(k):
        counter += total_available_products[i]

    print(counter)



