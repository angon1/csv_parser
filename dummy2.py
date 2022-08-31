def func():
    yield 'qwe'
    yield 'rgege'
    qwe = (yield)
    if qwe == True: 
        yield 'supa duap'

def func2():
    print('qwe')
    print('rgege')
    qwe = (yield)
    if qwe == True: 
        print('supa duap')
   
# x = func2()
# print(x)

# # print(next(x))
# # print(x.__next__())

# # print(list(x))
# # print(x)
# next(x)
# print('dupa')
# x.send(True)

list_c = [el*2 for el in range(10)]
gen_c = (el*2 for el in range(10))

print(gen_c)
# print(*(el for el in gen_c))
print(*gen_c, sep='\n')

def gen_c_my():
    for el in range(10):
        yield el*2
        
x = gen_c_my()
print(*x)