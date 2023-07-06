import math

testcase = int(input())
result = []

for i in range(testcase):
    n, m = map(int, input().split())
    result.append(math.factorial(m) // (math.factorial(n) * math.factorial(m - n)))

for i in result:
    print(i)