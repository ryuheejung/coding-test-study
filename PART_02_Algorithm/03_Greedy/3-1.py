# practice 3-1. change

change = 1260
count = 0

coins = [500, 100, 50, 10]

for coin in coins:
    count += change // coin
    change %= coin

print(count)