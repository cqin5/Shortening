
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def index(xy):
    """
    input a two-character string xy and return a base-2500 value
    """
    if len(xy) != 2:
        return 'Not a valid string'

    with open('ch.txt', encoding="utf-8") as file:
        chars = file.read()
        print(chars)
        for i in range(len(chars)):
            if chars.contains(xy[0]):  
                return 'Yeah'

def shorten(link):
    return 0;


raw = input("Please input some funny characters: ").decode("utf-8")
#decoded = raw.decode("utf-8")
#print(raw)
#print(decoded)
