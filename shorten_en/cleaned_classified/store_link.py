def __init__(self, link):

    # write to db and print an index
    db = open('db.txt').read().split()
    open('db.txt', 'a').write(link+'\n')

    # match index with word
    lib = open('lib.txt').read().split()


    #print("Match word is: "+ lib[len(db)])    
    #print('Index is: ' + str(len(db)))

    return lib[len(db)]
