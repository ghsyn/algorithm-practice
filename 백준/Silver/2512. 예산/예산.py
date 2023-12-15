town = int(input())
want = list(map(int, input().split()))
budget = int(input())

low, high = 0, max(want)

answer = 0
if sum(want) <= budget:
    answer = max(want)
else:
    while low <= high:
        total = 0
        mid = (low + high) // 2

        for i in want:
            total += min(i, mid)
        
        if total <= budget:
            low = mid + 1
            answer = mid
        else:
            high = mid - 1

print(answer)