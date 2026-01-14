import sys

data = sys.stdin.read().split()
        
n = int(data[0])
m = int(data[1])
    
s = set(data[2:2+n])
    
cnt = 0
for i in range(2+n, 2+n+m):
    if data[i] in s:
        cnt += 1
        
sys.stdout.write(str(cnt) + '\n')