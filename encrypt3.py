import math

def splitKey(key):
    keys = []
    chunk = ''
    for k in key:
        if k == ' ':
            keys.append(chunk)
            chunk = ''
        else:
           chunk+=k
    keys.append(chunk)
    return(keys)

def keyOrder(key):
    cur = 27
    order = []
    i = 0
    for k in key:
        if(ord(k) >= cur):
            cur = ord(k)
            order.append(i)
        else:
            spot = 0
            for o in range(len(order)):
                if(ord(key[order[o]]) < ord(k)):
                    spot = o+1
            order.insert(spot, i)
        i += 1
    return(order)

def updateTxt(key, step):
    order = keyOrder(key)
    output = ''
    for o in order:
        for s in step:
            output+=s[o]
    return(output)

def encrypt(txt, key):
    key = splitKey(key)
    for k in key:
        step = []
        for i in range(math.ceil(len(txt)/len(k))):
            line = ''
            for l in range(len(k)):
                if len(txt) > l+i*len(k):
                    line+=txt[l+i*len(k)]
                else:
                    line+='x'
            step.append(line)
        txt = updateTxt(k, step)
    return txt

def decrypt(txt, key):
    # [::-1] reverses list
    key = splitKey(key)[::-1]
    nextKey = 1
    for k in key:
        # create grid
        grid = []
        for i in k:
            grid.append('')
        line = ''
        x = 0
        y = 0
        for t in txt:
            line += t
            x += 1
            if x >= len(txt)/len(k):
                grid[keyOrder(k)[y]] = line
                line = ''
                y += 1
                x = 0
        
        #convert to txt
        temp = ''
        x = 0
        y = 0
        for t in range(len(txt)):
            temp += list(grid[y])[x]
            y += 1
            if y >= len(grid):
                y = 0
                x += 1

        #add spaces to make even
        temp = list(temp)
        if len(key) > nextKey:
            num = len(temp)/len(key[nextKey])
            while(not round(num) == num):
                # temp += 'x'
                temp.pop()
                num = len(temp)/len(key[nextKey])

        txt = ''.join(temp)
        nextKey += 1
    
    #remove spaces
    while(list(txt)[len(list(txt))-1] == 'x'):
        txt = txt[:-1]
    return(txt)

while True:
    print()
    t = input('Encrypt: ')
    k = input('Key: ')
    print("encrypted: "+encrypt(t, k))
    # print("decrypted: "+decrypt(encrypt(t, k), k))
    if t == decrypt(encrypt(t, k), k):
        print('SUCCESS!')
    else:
        print('FAIL! beleive it or not; jail.')