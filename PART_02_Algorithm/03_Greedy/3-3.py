# practice 3-3. number card game

n, m = map(int, input().split())

result = 0
min_list = []

for i in range(n):
    n_data = list(map(int, input().split()))

    min_list.append(min(n_data))

print(max(min_list))