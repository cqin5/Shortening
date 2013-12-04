verbs = open('verb_u.txt').read().split()

# Clean frequency and brackets
for i in range(len(verbs)):
    if verbs[i].isdigit():
        verbs.pop(i)
        verbs.insert(i, '')
    elif '(' in verbs[i]:
        verbs.pop(i)
        verbs.insert(i, '')
    elif ',' in verbs[i]:
        verbs.pop(i)
        verbs.insert(i, '')
    elif ')' in verbs[i]:
        verbs.pop(i)
        verbs.insert(i, '')

final=[]

for i in range(len(verbs)):
    if verbs[i] is not '':
        open('verb_c.txt', 'a').write(verbs[i]+'\n')

