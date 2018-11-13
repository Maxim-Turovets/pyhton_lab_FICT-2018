#handle = open("file.txt", "r")
#data = handle.readline()
data = "It is a long established, that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, content here, making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for lorem ipsum will uncover many web sites still in their infancy. Various versions have evolved over the years, sometime lispAnDpyhtonTheBest by accident, sometimes on purpose injected humour and the like."

def func(string):
    maxlen = 0
    for x in string.replace(',',' ').split():
        if len(x) > maxlen:
            maxlen = len(x)
            word = x
    print("Max word: "+word+"\nIts length: "+str(maxlen))


func(data)
#handle.close()