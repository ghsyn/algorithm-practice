pwd = input()
result = ''

con = ['a', 'e', 'i', 'o', 'u']

while (pwd != 'end'):
    con_cnt = 0
    vow_cnt = 0
    for i in range(len(pwd)):
        if len(pwd) < 1 or len(pwd) > 20:
            result += '<' + pwd + '>' + ' is not acceptable.\n'
            break
        elif not ('a' <= pwd[i] <= 'z'):
            result += '<' + pwd + '>' + ' is not acceptable.\n'
            break
        
        if not any(str in pwd for str in con):
            result += '<' + pwd + '>' + ' is not acceptable.\n'
            break
        
        if pwd[i] in con:
            vow_cnt = 0
            con_cnt += 1
        else:
            con_cnt = 0
            vow_cnt += 1
            
        if con_cnt == 3 or vow_cnt == 3:
            result += '<' + pwd + '>' + ' is not acceptable.\n'
            break
        
        elif i > 0 and ((pwd[i] == pwd[i - 1]) and (pwd[i] != 'e' and pwd[i] != 'o')):
            result += '<' + pwd + '>' + ' is not acceptable.\n'
            break
        
        elif i == len(pwd) - 1:
            result += '<' + pwd + '>' + ' is acceptable.\n'
            break
        
    pwd = input()

print(result)