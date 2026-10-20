s=input("Введите элементы через пробел")
s1=[int(i) for i in s.split()]

def f(x):
    b=[]
    for i in range(len(x)-1,-1,-1):
        b.append(x[i])
    return b

print(*f(s1))