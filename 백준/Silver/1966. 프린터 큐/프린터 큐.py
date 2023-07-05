testcase = int(input())

for _ in range(testcase):
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))
    index = [i for i in range(n)]
    count = 0
    
    while True:
        if importance[0] == max(importance):
            count += 1
            if index[0] == m:
                print(count)
                break
            else:
                del importance[0]
                del index[0]
        else:
            importance.append(importance[0])
            del importance[0]
            index.append(index[0])
            del index[0]