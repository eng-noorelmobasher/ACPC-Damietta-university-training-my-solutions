total, max_numbers = 0, 0

t = int(input())

for _ in range(t):
    
    total += int(input())

    max_numbers = max(max_numbers, total)

print(100 + max_numbers)