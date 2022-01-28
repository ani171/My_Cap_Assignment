def most_freq(x):
    d={}
    for i in x:
        d[i]=x.count(i)
    l=[]
    for j in d.values():
        l.append(j)
    l.sort()
    l.reverse()
    print(l)
    l1=[]
    for k in l:
        for a,b in d.items():
            if b==k:
                if a not in l1:
                    l1.append(a)
    for o in l1:
        print(o,end="")

n=input("Enter string")
most_freq(n)
