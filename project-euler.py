# Problem 1

sum = 0
n = 1

while n < 1000:
    if n % 3 == 0 or n % 5 == 0:
        sum += n
    n += 1

print(sum)
