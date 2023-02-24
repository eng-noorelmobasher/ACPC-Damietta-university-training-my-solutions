t = int(input())

for i in range(t):
    k, p, n = map(int, input().split())

    total_given = k * n
    total_solved = p * n

    omar_missed = total_given - total_solved
    #we will choose the maximum number between 0 and omar_missed
    #because omar cant solve problem more than given!, which mean the result is negative

    print(max(0,omar_missed))
    