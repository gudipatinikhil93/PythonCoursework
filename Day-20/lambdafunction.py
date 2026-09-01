#lambda syntax:
#variable = lambda argument: expression


wish = lambda name: f'Welcome to the course {name}'
print(wish('nikhil'))
print(wish('Prasad'))

gst = lambda price: price + price*0.18
print(gst(1000))
print(gst(2868))

avg = lambda a,b,c: (a+b+c)/3
print(avg(10,20,30))
print(avg(45,67,34))

iseven = lambda num: "even" if num%2==0 else 'odd'
print(iseven(10))
print(iseven(11))

largest = lambda a,b,c: a if a>b and a>c else (b if b>c else c)
print(largest(10,20,30))
print(largest(45,67,34))

isvowel = lambda a: 'vowel' if a in 'aeiouAEIOU' else 'consonant'
print(isvowel('a'))
print(isvowel('b'))


l = [1,2,3,4,5,6,7]
update = list(map(lambda i: i+10,l))
print(update)

t = (345,869,233,567,987,657)
discount = list(map(lambda i: i-i*0.3,t))
print(discount)


l2 = [2,3,4,5,6,7,8]
update = list(filter(lambda i: i%2!=0,l2))
print(update)

t2 = (342,657,233,567,875,346,775)
great = list(filter(lambda i: i>500,t2))
print(great)


l = ['nikhil@codegnan.com','nikhil@gmail.com','nikhil@yahoo.com','nikhil@outlook.com']
domain = list(map(lambda i: i.split('@')[1],l))
print(domain)


from functools import reduce

l = [23,54,677,45,2343,5,76]

res = reduce(lambda sum,i:sum+i,l)
print(res)

res2 = reduce(lambda prod2,i:prod2*i,l)
print(res2)


seats = {'s1':True,
         's2':False,
         's3':True,
         's4':False,
         's5':True,
         's6':True,
         }

avail = list(filter(lambda i:seats[i]==True,seats))
print(avail)

prod = {
    'eggs':80,
    'milk':50,  
    'bread':30,
    'butter':100,
    'salt':20
}

res3 = list(filter(lambda i:prod[i]>50,prod))
print(res3)

print(dict(sorted(prod.items(),key= lambda i:i[1])))
print(dict(sorted(prod.items(),key= lambda i:i[1],reverse=True)))