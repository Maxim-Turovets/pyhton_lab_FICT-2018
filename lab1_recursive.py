#step ="12345"

s = 0
i = 0

def recursive():
    global i
    global s
    step = str(2**1000)
    sa = list(step)
    count = len(sa) 

    if i<count:
        s+=int(sa[i])
        i = i + 1
        return recursive()
    
recursive()    
print (s)