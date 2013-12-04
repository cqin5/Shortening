#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def get_index(xyz):
    """
    input a two-character string xy and return a base-2500 value
    """
    cnlib = []
    xyz = xyz.decode('utf-8')
    chars = open('ch.txt').read().split()
    [chars[i].decode('utf-8') for i in range(len(chars))]
    baseX = len(chars)
    value = 0

    if len(xyz) is 1:
        for i in range(len(chars)):
            if xyz[0].encode('utf-8') in chars[i]:
                value += 1*(i+1)
                print(value)
                return value
                pass
		
		
    if len(xyz) is 2:
        for i in range(len(chars)):
            if xyz[0].encode('utf-8') in chars[i]:
                value = baseX**(len(xyz)-1)*(i+1)
                break
        for i in range(len(chars)):
            if xyz[1].encode('utf-8') in chars[i]:
                value += baseX**(len(xyz)-1-1)*(i+1)
                print(value)
                return value
                pass
                
    if len(xyz) is 3:
        for i in range(len(chars)):
            if xyz[0].encode('utf-8') in chars[i]:
                value = baseX**(len(xyz)-1-0)*(i+1)
                break
        for i in range(len(chars)):
            if xyz[1].encode('utf-8') in chars[i]:
                value += baseX**(len(xyz)-1-1)*(i+1)
                break
        for i in range(len(chars)):
            if xyz[1].encode('utf-8') in chars[i]:
                value += baseX**(len(xyz)-1-2)*(i+1)
                print(value)
                return value
                pass
    
    if len(xyz) != 1 or 2 or 3:
        print('Not a valid string')
        return -1
        pass


"""
def get_char(index):
    """
   # get the Chinese characters corresponding to the index
"""
    chars = open('ch.txt').read().split()
    [chars[i].decode('utf-8') for i in range(len(chars))]
    
    print((493101417900/(7900**2)-1))

    if index <= 7900:
    	print(chars[index-1])
        return chars[index-1]
    elif index <= 62417900:
        temp = []
        temp.append(chars[index%7900 -1])
        temp.insert(0, chars[(index/7900)%7900 -1])
        print(''.join(temp))
        return ''.join(temp)
    elif index <= 493101417900: 
        temp = []
        temp.append(chars[index%7900 -1])
        temp.insert(0, chars[(index/7900)%7900 -1])
        temp.insert(0, chars[index/(7900**2)-1])
        print(''.join(temp))
        return ''.join(temp)
        
    [temp[i].decode('utf-8') for i in range(len(temp))]

            
    return 0

"""
    
def shorten(link):
    """
    input a string of link, return an index from 1 to 493,101,417,900 (7900^3 + 7900^2 + 7900)
    """
    file = open('list.txt', 'a')
    next_pointer = open('list.txt').read().split()

    file.write(link + "\n")
    
    file.close()
    
    print(len(open('list.txt').read().split()))
    return len(open('list.txt').read().split()) 



def crazy_lib():
    """
    creates a library of 3-character combinations (7900^3)
    """
    list = open('list.txt').read()
    [list[i].decode('utf-8') for i in range(len(list))]
    
    lib = open('lib_all.txt','a')

    for i in range(len(list)):
        for j in range(len(list)):
            for k in range(len(list)):
                lib.write(list[i] + list[j]+ list[k] + '\n')
    

#get_index('㸌㸌一')
#get_char(493101417900)
#print((493101417900/(7900**2)-1))
#shorten_link('www.teewlktjaehtlacom.com')

crazy_lib()
