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
  
#task 15


# Task 3

def func(a, b):
 return a + b

# Вспомогательная функция частичного применения. Нужна для того, чтобы закрепить в m-местной функции первые n (n<m) аргументов. 
# нужна для того, чтоб превращать функции двух переменных в функции одной переменной, закрепляя первый аргумент.
# Например, функцию f(a, b) = 2a + 3b можно превратить, скажем, в f(b) = 10 + 3b, если вызвать part_apply(f, 5)
def part_apply(fn, *args):
 return lambda *other: fn(*args, *other)



# функция применяет переданную ей одноместную функцию на массив последовательных натуральных чисел (1, 2, 3, ...). 
# Нужна для того, чтоб построить строку матрицы
def create_row(fn, st_c, cq):
 return list(map(fn, list(range(st_c, st_c + cq))))




# функция создает, собственно матрицу, последовательно вызывая функцию create_row
def create_matrix(fn, st_r, st_c, rq, cq):
 return list(map(lambda num: create_row(part_apply(fn, num), st_c, cq),
  list(range(st_r, st_r + rq))))


# конструктор функций в зависимости от количества параметров
def matrix_constructor(fn, *args):
 if len(args) == 0:
  return lambda r, c: create_matrix(fn, 0, 0, r, c)
 if len(args) == 2:
  return lambda r, c: create_matrix(fn, args[0], args[1], r, c)
 if len(args) == 4:
  return create_matrix(fn, args[0], args[1], args[2], args[3])

# вывод в более читабельной форме
def my_print(a):
 for i in range(len(a)):
     for j in range(len(a[i])):
         print(a[i][j], end=' ')
     print()


cons = matrix_constructor(func)
my_print(cons(3, 4))
print("====================")

cons = matrix_constructor(func, 2, 2)
my_print(cons(3, 4))
print("====================")

my_print(matrix_constructor(func, 2, 2, 4, 5))
print("====================")
  
  
