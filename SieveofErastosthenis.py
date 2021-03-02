def sieveofErastosthenis(n):
    q=[]
    c=0
    prime=[True for i in range(n+1)]
    p=2
    while(p*p<n+1):
        if prime[p]==True:
            for j in range(p*p,n+1,p):
                prime[j]=False
        p+=1
    for i in range(2,n+1):
        if prime[i] and n%i==0:
            c+=1
            q.append(i)
    print(q)
    return c
if __name__=="__main__":
    n=int(input("Enter the no. upto which you want primes:"))
    c=sieveofErastosthenis(n)
    print(c)