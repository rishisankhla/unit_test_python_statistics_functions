def standard2(testlist):
    mean = sum(testlist) / len(testlist)
    variance = sum([((x - mean) ** 2) for x in testlist]) / len(testlist)
    result = variance ** 0.5
    return result

def standard1(testlist):
    mean = sum(testlist) / len(testlist)
    variance = sum([((x - mean) ** 2) for x in testlist]) / len(testlist)
    result = variance 
    return result

def variance1(testlist):
    mean = sum(testlist) / len(testlist)
    result = sum((i - mean) ** 2 for i in testlist) 
    return result

def variance2(testlist):
    mean = sum(testlist) / len(testlist)
    result = sum((i - mean) ** 2 for i in testlist) / len(testlist)
    return result

def median2(testlist):
    if len(testlist)%2==1:
        i=0
        g=0
        h=len(testlist)-1
        while i<len(testlist):
            if g==h:
                break
            if i%2==0:
                g=g+1
            else:
                h=h-1
            i=i+1
        result=testlist[g]
    else:
        i1=int(len(testlist)/2)
        i2=i1-1
        result=testlist[i2]+testlist[i1]
        result=result/2
    return result

def median1(testlist):
    listlen=len(testlist)-1
    listlen=listlen/2
    result=testlist[int(listlen)]
    return result

def mean2(testlist):
    v=0
    for i in testlist:
        v=i+v
    result=v/len(testlist)
    return result

def mean1(testlist):
    a=testlist[0]
    b=testlist[1]
    c=testlist[2]
    d=testlist[3]
    return (a+b+c+d)/len(testlist)

def mode2(testlist):
    p={}
    for i in testlist:
        if i in p:
            p[i]=p[i]+1
        else:
            p[i]=1
    result=max(zip(p.values(), p.keys()))[1]
    return result

def mode1(testlist):
    p={}
    for i in testlist:
        if i in p:
            p[i]=p[i]+1
        else:
            p[i]=1
    result=max(zip(p.vales(), p.keys()))[1]
    return result  

def harmonicmean2(testlist):
    c=0
    for i in testlist:
        c=c+(1/i)
    result=len(testlist)/c
    return result

def harmonicmean1(testlist):
    c=0
    counter=1
    for i in testlist:
        c=(c+(1/i))
        counter=counter+1
    result=counter/c
    return result

def groupedmedian2(testlist):
    i1=int(len(testlist)/2)
    i2=i1-1
    result=testlist[i2]+testlist[i1]
    return result/2

def groupedmedian1(testlist):
    i1=len(testlist)/2
    i2=i1-1
    result=testlist[i2]+testlist[i1]
    return result/2

def medianhigh2(testlist):
    i=0
    while len(testlist)!=2:
        if i==0:
            i=1
            del testlist[0]
        else:
            i=0
            del testlist[-1]
    result=testlist[1]
    return result

def medianhigh1(testlist):
    i=0
    while i<len(testlist):
        if len(testlist)==2:
            break
        if i%2==0:
            del testlist[0]
        else:
            del testlist[-1]
        i=i+1
    result=testlist[1]
    return result

def max2(testlist):
    y=0
    for i in testlist:
        if y<i:
            y=i
    result=y
    return result

def max1(testlist):
    a=testlist[0]
    b=testlist[1]
    c=testlist[2]
    d=testlist[3]
    r=0
    if a>b:
        r=a
    else:
        r=b
    if c>r:
        r=c
    if d>r:
        r=d
    result=r 
    return result
