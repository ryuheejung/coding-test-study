# practice 4-1. up down left right

space_n = int(input())
plans = input().split()

location_a = [1, 1]

def move_udlr(location: tuple, movement: str):
    if movement == "U" and location[0]>1:
        location[0] -= 1
    if movement == "D" and location[0]<space_n:
        location[0] += 1
    if movement == "L" and location[1]>1:
        location[1] -= 1
    if movement == "R" and location[1]<space_n:
        location[1] += 1

for plan in plans:
    move_udlr(location_a, plan)

print(location_a[0], location_a[1])
