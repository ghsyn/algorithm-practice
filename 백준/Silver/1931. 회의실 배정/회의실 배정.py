n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
times.sort()
times.sort(key = lambda x: x[-1])

end = times[0][1]
cnt = 1

for i in range(1, n):
    if(end <= times[i][0]):
        end = times[i][1]
        cnt += 1
print(cnt)