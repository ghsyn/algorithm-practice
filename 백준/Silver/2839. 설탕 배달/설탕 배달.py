n = int(input())

count = n // 5
n %= 5

while count >= 0:
    if n % 3 == 0:
        count += n // 3
        print(count)
        break
    else:
        count -= 1
        n += 5
else:
    print('-1')