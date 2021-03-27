
'''
ID: smaylni1
LANG: PYTHON3
TASK: namenum
'''

chars = {2 : ['A', 'B', 'C'], 3 : ['D', 'E', 'F'], 4 : ['G', 'H', 'I'], 5 : ['J', 'K', 'L'], 6 : ['M', 'N', 'O'],
         7 : ['P', 'R', 'S'], 8 : ['T', 'U', 'V'], 9 : ['W', 'X', 'Y']}

f = open('namenum.in', 'r')
numbers = f.read().rstrip('\n')
f.close()

numbers = str(numbers)

f = open('dict.txt', 'r')
data = f.read().split('\n')
f.close()

data_new = []

for i in range(0, len(data)):
    if i < len(data):
        if len(data[i]) == len(numbers):
            data_new.append(data[i])

data = []
fl = 0
f = open('namenum.out', 'a')

for i in range(0, len(data_new)):
    k = 0
    while (k < len(numbers)):
        if data_new[i][k] in chars[int(numbers[k])]:
            k += 1
            continue
        else:
            break
    if (k == len(numbers)):
        fl = 1
        f.write(data_new[i] + '\n')

if (fl != 1):
    f.write('NONE\n')

f.close()