# print('Hello', 'World!')

print('Hello', 'World!') # print Hello World!
print('Hello', 'World!') # print Hello World!
print('Hello', 'World!') # print Hello World!

# print Hello World!
print(
    'Hello', 
    'World!'
    ) 

if 3 > 2:
    print('Yes 3 > 2')

    if 4>3:
        print('but 3 < 4')

print('Hello, John!')   

# print Number of 0 to 10
# for i in range(10):
    # print(i)

a = 1
b = 2
c = 5.6

s = "Hello, John!"

print(a,b,c,s)

a = 'aaaa'

print('a:', type(a))
print('b:', type(b))
print('c:', type(c))
print('s:', type(s))

b = float(b)
c = str(c)
d = int(2.7)

print('b:', type(b), b)
print('c:', type(c), c)
print('d:', type(d), d)

print(a is b)

l = [1, 2, 3, 'b', 'c', 5.2]

print(l[0])

print(len(l))

print(l[len(l)-1])

l.append('asd')
# l[6] = 'asdasd'

print(l)

def sum(a,b):
   # first solution
   # if type(a)==str or type(b)==str:
   #     return 0
   # else:
    
   # second solution
    if type(a) != float or type(a) != int:
        return 0
    if type(b) != float or type(b) != int:
        return 0
    
    return a + b
e = sum(5, 9)

print('SUM:', e)

if 1 > 2:
    print('1 > 2')
else:
    print('2 > 1')

if 1 > 2:
    print('1 > 2')
elif 1 > 0.5:
    print('1 > 0.5')
else:
    print('1 < 2 and < 0.5')

result = sum(1, '2')

print(result)

def foo(a):
    print('a:', a)
    a.append('11111111111')
    a.append('2222')

def fool(a):
    a = 333

foo(l)

print('List: ', l)

fool(b)
print(b)

f = {
    'a': 100,
    'b': 200,
    'c': 250,
}

print(type(f))
print(f)

