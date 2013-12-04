from collections import OrderedDict

adj = open('adj_c.txt').read().split()
adv = open('adv_c.txt').read().split()
noun = open('noun_c.txt').read().split()
prep = open('prep_c.txt').read().split()
pronoun = open('pronoun_c.txt').read().split()
verb = open('verb_c.txt').read().split()
           
lib_all = adj + adv + noun + prep + pronoun + verb

print('starting...')
# adj + noun
for i in range(len(adj)):
    temp = ''
    for c in range(len(noun)):
        temp = adj[i] + '-' + noun[c]
        lib_all.append(temp)
print('1')

# adv + adj
for i in range(len(adv)):
    temp = ''
    for c in range(len(adj)):
        temp = adv[i] + '-' + adj[c]
        lib_all.append(temp)
print('2')
# adv + verb
for i in range(len(adv)):
    temp = ''
    for c in range(len(verb)):
        temp = adv[i] + '-' + verb[c]
        lib_all.append(temp)
print('3')
# verb + noun
for i in range(len(verb)):
    temp = ''
    for c in range(len(noun)):
        temp = verb[i] + '-' + noun[c]
        lib_all.append(temp)
print('4')
# noun + noun
noun_lower = noun
for i in range(len(noun)):
    temp = ''
    for c in range(len(noun_lower)):
        temp = noun[i] + '-' + noun_lower[c]
        lib_all.append(temp)
print('5')
# verb + verb
verb_lower = verb
for i in range(len(verb)):
    temp = ''
    for c in range(len(verb_lower)):
        temp = verb[i] + '-' + verb_lower[c]
        lib_all.append(temp)
print('6')


# print size
print(len(lib_all))


# remove duplicates
lib_all_noduplicate = list(set(lib_all))
print(len(lib_all_noduplicate))


longest = 0
longest_word = ''
for i in range(len(lib_all_noduplicate)):
    if i == 0:
        longest = len(lib_all_noduplicate[0])
        longest_word = lib_all_noduplicate[0]
    else:
        if len(lib_all_noduplicate[i]) > longest:
            longest = len(lib_all_noduplicate[i])
            longest_word = lib_all_noduplicate[i]
print(str(longest))
print(longest_word)

# write lib
lib = open('lib.txt', 'w')
for i in range(len(lib_all_noduplicate)):
    lib.write(lib_all_noduplicate[i]+'\n')
lib.close()

# print done
print('done')
