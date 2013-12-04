UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


words = open('list2.txt').read().split()

#print(words)

CC = []
CD = []
DT = []
IN = []
JJ = []
NN = []
PRP = []
RB = []
RP = []
TO = []
UH = []
VB = []

merged = []


for i in range(len(words)):
    if 'CC' in words[i]:
        CC.append(words[i])
    elif 'CD' in words[i]:
        CD.append(words[i])
    elif 'DT' in words[i]:
        DT.append(words[i])
    elif 'IN' in words[i]:
        IN.append(words[i])
    elif 'JJ' in words[i]:
        JJ.append(words[i])
    elif 'NN' in words[i]:
        NN.append(words[i])
    elif 'PRP' in words[i]:
        PRP.append(words[i])
    elif 'RB' in words[i]:
        RB.append(words[i])
    elif 'RP' in words[i]:
        RP.append(words[i])
    elif 'TO' in words[i]:
        TO.append(words[i])
    elif 'UH' in words[i]:
        UH.append(words[i])
    elif 'VB' in words[i]:
        VB.append(words[i])
    elif 'WP' in words[i]:
        PRP.append(words[i])

print('Adj: ' + str(len(JJ)))
print('Verb: ' + str(len(VB)))
print('Adv: ' + str(len(RB)))
print('Noun: ' + str(len(NN)))
print('Pronoun: ' + str(len(PRP)))
print('Noun: ' + str(len(NN)))

blank = ['']
merged = CC + blank + CD + blank + DT + blank + IN + blank + JJ + blank + NN + blank + PRP + blank + RB + blank + RP + blank + TO + blank + UH + blank + VB


cleaned = []
string = ''

for i in range(len(merged)):
    if "/" in merged[i]:
        for s in range(len(merged[i])):
            if merged[i][s] is not "/":
                string = string + merged[i][s]
            else:
                cleaned.append(string)
                string = ''
                break
    else:
        cleaned.append(merged[i])
#print(cleaned)

file = open('cleaned.txt', 'a')

for i in range(len(cleaned)):
    file.write(cleaned[i] + '\n')

file.close()
