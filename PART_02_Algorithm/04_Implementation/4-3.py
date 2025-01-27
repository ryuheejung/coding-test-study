# practice 4-3. Night of kingdom
# column: a-h, row: 1-8

location_night = input()
location_column = int(ord(location_night[0]))-int(ord("a")) + 1
location_row = int(location_night[1])

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, 2), (-1, -2)]

case = 0

for step in steps:
    new_column = location_column + step[0]
    new_row = location_row + step[1]
    if new_column > 0 and new_row > 0:
        case += 1

print(case)
