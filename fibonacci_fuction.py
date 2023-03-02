
def fibbonacci(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n<1:
        pass
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)

fibbonacci(12)