def solution(items):
    for i in range(9):
        for j in range(i+1, 9):
            if (result == items[i] + items[j]):
                items.pop(i)
                items.pop(j - 1)
                return items
            else:
                continue
            
if __name__ == "__main__":
    items = []
    result = 0

    for _ in range(9):
        items.append(int(input()))
        
    result = sum(items)
    result -= 100
    
    solution(items)
            
    for i in items:
        print(i)