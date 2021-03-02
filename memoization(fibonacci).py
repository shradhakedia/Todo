fib_cache={}
def fibonacci(n):
    #if cache dictionary has value use it i.e. return it
    if n in fib_cache:
        return fib_cache[n]
    #compute the nth term
    if n==1 or n==2:
        value=1
    elif n>2:
        value=fibonacci(n-1)+fibonacci(n-2)
    fib_cache[n]=value
    return value
for i in range(1,1000):
    print(i,":",fibonacci(i))
