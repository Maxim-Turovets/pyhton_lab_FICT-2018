#task 4
string = "lorem! ipsum! sit amet consectetur adipisicing elit itaque omnis inventore dolor voluptas totam nobis"
r=string.split(' ')
i=0

def func():
    global i
    global r

    r[i]=r[i].strip('!')
    i=i+1
        
    if(i<len(r)):
         return func()

r.sort()         
func()  
print(r)   



#task 5
import math
list_=[5,3,9,23,22,14,16,56,25,81,231,144,45,21,225]
i=0


def func():
    global i
    global list_
    b=(math.sqrt(list_[i]))
   
    if (b.is_integer()==True):
        print(list_[i])
    i=i+1
        
    if(i<len(list_)):
         return func()    
  
    
func()
  
  