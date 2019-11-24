
data = "It is a long established, that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, content here, making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for lorem ipsum will uncover many web sites still in their infancy. Various versions have evolved over the years, sometime LispAndPyhtonTheBest by accident, sometimes  on purpose injected a humour and the like."

maxlen = 0
i=0
word=""
def recursive(string):
    global maxlen
    global i
    global word
    str2 = string.replace(',',' ').split()
    count =len(str2) 
    if i<count-2:
        if len(str2[i]) >  maxlen:
                maxlen = len(str2[i])
                word = str2[i]
        i = i + 1
        return recursive(data)
    else:
        print("Max word: "+word+"\nIts length: "+str(maxlen))
        return 
    
recursive(data)

