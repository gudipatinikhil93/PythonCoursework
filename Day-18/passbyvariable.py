#int float complex str tuple bool = they give different output inside and outside the function because they are passed by value

#list dict set = mutable, so they give same output inside and outside the function because they are passed by reference

#int
def display(n):
    n+=10
    print('Inside function: ',n)

n=10
display(n)
print('Outside function: ',n)


#float
def display(n):
    n+=6.7
    print('Inside function: ',n)

n=6.9
display(n)
print('Outside function: ',n)


#complex
def display(n):
    n+=10
    print('Inside function: ',n)

n=34+5j
display(n)
print('Outside function: ',n)


#str
def display(n):
    n+=' lang'
    print('Inside function: ',n)

n='python'
display(n)
print('Outside function: ',n)


#list
def display(n):
    n.append(3)
    print('Inside function: ',n)

n=[7,5,6,1,8]
display(n)
print('Outside function: ',n)
#same output because list is mutable and it is passed by reference


#set
def display(n):
    n.add(6)
    print('Inside function: ',n)

n={5,2,9,1}
display(n)
print('Outside function: ',n)
#same output because set is mutable and it is passed by reference


#dict
def display(n):
    n[5]=6
    print('Inside function: ',n)

n={1:2,3:4}
display(n)
print('Outside function: ',n)
#same output because dict is mutable and it is passed by reference


#bool
def display(n):
    n=False
    print('Inside function: ',n)

n=True
display(n)
print('Outside function: ',n)



