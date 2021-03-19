def sieveofErastosthenis(n):
    prime=[0 for i in range(n+1)]
    p=2
    while(p<n+1):
        if prime[p]==0:
            for j in range(p,n+1,p):
                prime[j]+=1
        p+=1
    cp=[[0]*11 for i in range(5)]
    for i in range(1,5):
        for j in range(2,11):
            if prime[j]==i:
                cp[i-1][j]=cp[i-1][j-1]+1
            else:
                cp[i-1][j]=cp[i-1][j-1]
    print(cp)
    return prime
if __name__=="__main__":
    n=int(input("Enter the no. upto which you want to count primes:"))
    q=sieveofErastosthenis(n)
    print(q)