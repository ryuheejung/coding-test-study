# practice 3-4. until them become 1

n, k = map(int, input().split())

result = 0

while True:
    if n == 1:
        print(result)
        break
    if n%k == 0:
        n //= k
        result += 1
    else:
        n -= 1
        result += 1
