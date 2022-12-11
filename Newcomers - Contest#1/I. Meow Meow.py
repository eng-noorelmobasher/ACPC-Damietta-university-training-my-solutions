n = int(input())

lst = list(map(int, input().split()))

#we will print the SECOND largest number
#we have to sort first!

lst.sort()

i = n - 1
while lst[i] == lst[-1]:
    i -= 1

print(lst[i])