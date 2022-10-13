#Variable no of arguments

#!/usr/bin/python3

def nargs(arg1,*argn):
    print(arg1)
    print(type(argn))
    print(argn)
    mylist=list(argn)
    print(mylist)
nargs(10,20,30,40,50,60,70,80,90,100)
