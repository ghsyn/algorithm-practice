list = input()
max = ""
min = ""

data = 0
for i in list:
    if(i == "K"):
        if data > 0:
            max += str(5 * 10 ** data)
            min += str(1 * 10 ** data + 5)
            data = 0
        else:
            max += "5"
            min += "5"
    else:
        data += 1
if data > 0:
    max += "1" * data
    min += str(1 * 10 ** (data - 1))
    
print(max)
print(min)