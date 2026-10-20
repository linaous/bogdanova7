s=input("Введите элементы через пробел")
s1=[int(x) for x in s.split()]

def f(x):
    x.sort()
    b=[]
    n=len(x)
    for l in range(n-2):
        if l>0 and x[l]==x[l-1]:
            continue
        i=l+1
        r=n-1
        while i<r:
            s=x[l]+x[i]+x[r]
            if s==0:
                b.append([x[l],x[i],x[r]])
                while i<r and x[i]==x[i+1]:
                    i+=1
                while i<r and x[r]==x[r-1]:
                    r-=1
                i+=1
                r-=1
            elif s<0:
                i+=1
            else:
                r-=1
    return b
for t in f(s1):
    print(*t)

    