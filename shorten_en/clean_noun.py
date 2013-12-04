words = open('pronoun_u.txt').read().split()

# Clean frequency and brackets
for i in range(len(words)):
    if words[i].isdigit():
        words.pop(i)
        words.insert(i, '')
    elif '(' in words[i]:
        words.pop(i)
        words.insert(i, '')
    elif ',' in words[i]:
        words.pop(i)
        words.insert(i, '')
    elif ')' in words[i]:
        words.pop(i)
        words.insert(i, '')

for i in range(len(words)):
    if words[i] is not '':
        open('pronoun_c.txt', 'a').write(words[i]+'\n')

