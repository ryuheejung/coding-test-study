# practice 4-2. clock with num 3
# 00(h) 00(m) 00(s)~ n(h) 59(m) 59(s)

int_n = int(input())

# the number of cases per hour
case_n = 0

for hour in range(int_n+1):
    for min in range(60):
        for sec in range(60):
            hour_min_sec = str(hour)+str(min)+str(sec)
            if "3" in hour_min_sec:
                case_n += 1

print(case_n)
