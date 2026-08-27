
#syntax of recursion
def function_name(parameters):
    if base:
        return
    function_name(modified_parameters)


def display(n):
    if n==11:
        return
    print(n)
    display(n+1)

display(1)


def display(n):
    if n==0:
        return
    print(n)
    display(n-1)

display(10)


def display(n,i):
    if i==len(n):
        return
    print(n[i])
    display(n,i+1)
    
display('codegnan',0)


