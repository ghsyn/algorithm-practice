n = int(input())
prices = []

for _ in range(n):
    item = int(input())
    prices.append(item)
    
prices.sort(reverse=True)
result = 0

for i in range(n):
    if (i % 3 != 2):
        result += prices[i]
        
print(result)