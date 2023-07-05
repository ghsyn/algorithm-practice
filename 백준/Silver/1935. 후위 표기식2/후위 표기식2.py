N = int(input())
operator = input()
val_list = [0]*N

for i in range(N):
    val_list[i] = int(input())
    
stack = []

for i in operator:
    if 'A' <= i <= 'Z':
        stack.append(val_list[ord(i) - ord('A')])
    else:
        val2 = stack.pop()
        val1 = stack.pop()
        
        if i == '+':
            stack.append(val1 + val2)
        elif i == '-':
            stack.append(val1 - val2)
        elif i == '*':
            stack.append(val1 * val2)
        elif i == '/':
            stack.append(val1 / val2)
            
print('%.2f' %stack[0])