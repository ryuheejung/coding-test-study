# practice 3-2. The rule of big number

limit_time = 1

n, m, k = map(int, input().split())
n_data = list(map(int, input().split()))

n_data.sort()

n_first = n_data.pop()
n_second = n_data.pop()

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += n_first
        m -= 1
    if m == 0:
        break
    result += n_second
    m -= 1

print(result)
