def num(a):
    print('The Original List:',a)
    b=[]
    c=[]
    for i in a:
        if (i%2)==0:
            b.append(i)
        else:
            c.append(i)
    print('Even Numbers In The List:',b)
    print('Odd Numer In The List:',c)
n=[12,11,13,33,24,35,38,10,22,78]
num(n)

