n = int(input())
times = list(map(int, input().split()))

result = 0
times.sort()
for i in range(n):
    result += sum(times[0:i + 1])
    
print(result)