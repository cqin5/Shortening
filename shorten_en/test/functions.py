import timeit # to calculate processing time

def get_link(keyword):
    """
    based on the parameter, return the position
    """
    db = open('db.txt').read().split()
    lib = open('lib.txt').read().split()

    for i in range(len(lib)):
        if lib[i] == keyword:
            print(db[i])
            return db[i]


def store_link(link):

    # write to db and print an index
    db = open('db.txt').read().split()
    open('db.txt', 'a').write(link+'\n')

    # match index with word
    lib = open('lib.txt').read().split()


    print("Match word is: "+ lib[len(db)])    
    print('Index is: ' + str(len(db)))

    return lib[len(db)]



get_link(store_link('http://stackoverflow.com/questions/1504717/why-does-comparing-strings-in-python-using-either-or-is-sometimes-produce'))



