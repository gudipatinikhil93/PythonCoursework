from datetime import date,time,datetime,timedelta

t = date.today()

print(t)
print(t.day)
print(t.month)
print(t.year)
print(t.weekday())

year,month,day = list(map(int,input('[YYYY-MM-DD]: ').split('-')))
print(date(year,month,day))


tm = time(23,6,6)

print(tm)
print(tm.hour)
print(tm.minute)
print(tm.second)


dt = datetime.now()

print(dt)
print(dt.strftime('%d-%m-%y')) #05-09-26
print(dt.strftime('%d-%m-%Y')) #05-09-2026
print(dt.strftime('%d-%m-%Y %H:%M:%S')) #05-09-2026 17:44:04
print(dt.strftime('%d-%m-%Y %H:%M:%S %p')) #05-09-2026 17:44:04 PM
print(dt.strftime('%d-%m-%Y %I:%M:%S %p')) #05-09-2026 05:44:04 PM
print(dt.strftime('%d-%b-%Y %I:%M:%S %p')) #05-Sep-2026 05:44:04 PM
print(dt.strftime('%d-%B-%Y %I:%M:%S %p')) #05-September-2026 05:44:04 PM
print(dt.strftime('%a, %d %B %Y %I:%M:%S %p')) #Sat, 05 September 2026 05:44:04 PM
print(dt.strftime('%A, %d %B %Y %I:%M:%S %p')) #Saturday, 05 September 2026 05:44:04 PM


dt1 = datetime.now()
t1 = date.today()

t7 = t1 + timedelta(days=7)
print(t7)

m15 = dt1 + timedelta(minutes=15)
print(m15)


from itertools import permutations,combinations

s = 'abc'

res1 = list(permutations(s,2))
res2 = list(combinations(s,2))

print([''.join(i) for i in res1])
print([''.join(i) for i in res2])
