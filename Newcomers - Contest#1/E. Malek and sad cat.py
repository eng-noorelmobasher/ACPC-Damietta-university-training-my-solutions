n = int(input())

primes = []

#firstly we will get the prime numbers from 1 to n.

for i in range(2,n+1):

    check = True
    for j in range(2,int(i**0.5)+1):

        if i % j == 0:
            check = False
            break
    if check:
        primes.append(i)

#secondly we will count the numbers that is divisible by ONLY two prime numbers
global_counter = 0
for i in range(1,n+1):
    counter = 0
    for j in primes:

        if i % j == 0:
            counter += 1
            
    if counter == 2:
        global_counter += 1

print(global_counter)