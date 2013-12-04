def __init__(self, keyword):

    db = open('db.txt').read().split()
    lib = open('lib.txt').read().split()

    for i in range(len(lib)):
        if lib[i] == keyword:
            #print(db[i])
            return db[i]
