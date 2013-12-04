UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


words = open('list2.txt').read().split()

print(words)


for i in range(len(words)):
    #print(i)
    if "'" in words[i]:
        words.pop(i)
        words.insert(i, '')
    elif '.' in words[i]:
        words.pop(i)
        words.insert(i, '')
    elif words[i][0] in UPPER:
        words.pop(i)
        words.insert(i, '')


file = open('list1.txt', 'a')

for i in range(len(words)):
    if words[i] is not '':
        write = file.write(words[i]+'\n')
file.close()

