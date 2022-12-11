n = int(input())

troops_code = list(map(int, input().split()))

#we cant loop on the list then reduce each element by one
#because this way you will exceed the time limit..
#we can solve it in math!

#first we want to know how many even and odd numbers in the list

even , odd = 0 , 0

for i in troops_code:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

common = min(odd, even)
odd -= common
even -= common

if even:
    result = common * 2 + (even * 2 - 1)
else:
    result = common * 2 + (odd * 2)

print(result)

