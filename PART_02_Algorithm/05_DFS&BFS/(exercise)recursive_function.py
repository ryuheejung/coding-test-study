# page.132
# 5-5.py 2가지 방식으로 구현한 팩토리얼 예제

# recursive function
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)
# iterative function
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print("5 factorial :")
print("recursive result", factorial_recursive(5))
print("iterative result", factorial_iterative(5))
