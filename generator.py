def hello():
    yield 1
    yield 2
    yield 3
hellItem = hello()
print(next(hellItem))
print(next(hellItem))

def myrange(end):
    count = 0
    while count <= end:
        yield count
        count+=1

a = [1,2,3,4]
for i in myrange(10):
    print(i)

def balls():
    for i in range(1000000000000):
        yield i

ballres = balls()
# print(next(ballres))
# print(next(ballres))

for item in range(100):
    print(next(ballres))





   

