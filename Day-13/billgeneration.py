data = {
    'suger' : 40,
    'wheat_flour' : 45,
    'groudnuts' : 150,
    'milk' : 32,
    'eggs' : 7,
    'bread' : 50,
    'biscuits' : 10
}

for i in data:
    print(i.ljust(15),data[i])

total = 0
prod = input('Enter products: ').split()
for i in prod:
    print(f'{i.ljust(20)} {data.get(i)}')
    total = total+data.get(i)
print('Total is: '.ljust(20),total)





    
    

