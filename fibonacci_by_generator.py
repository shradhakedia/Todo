def fibonacci(n):
    '''
    generators are functions that yield instead of return. They are the iterator that is we can 
    yield many values one by one. it isn't called always but store all the yields value and gives on iteration.
    '''
    i=0
    j=1
    print(i) #printed once
    print(j) #printed once
    for _ in range(n): #loop to get all fibonacci nos.
        k=i+j 
        i=j 
        j=k
        yield k
g=fibonacci(10) #g is iterator
print(g)
for x in g:
    print(x)