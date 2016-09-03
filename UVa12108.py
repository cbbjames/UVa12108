from sys import stdin
def over_half(table,cnt):
    num=0
    for row in range(len(table)):
        if(table[row][cnt]==0):num+=1
    if(num==0): return 0
    elif(num>len(table)-num):return 1
    else: return -1

kase=1

for line in stdin:
    n=int(line)
    if(n==0) : break
    table=[]
    stu=[]

    class student:
        t=[]
        r=[]

    for i in range(n):
        s=input()
        sp=s.split()
        a=int(sp[0])
        b=int(sp[1])
        c=int(sp[2])
        c-=1
        one=[a,b,c]
        t=[]
        for _ in range(a): t.append(0)
        for _ in range(b): t.append(1)

        d=student()
        d.r=one
        d.t=t
        stu.append(d)

        f=[]
        if(c>=a):
            for _ in range(c,a+b):
                f.append(0)
            for _ in range(a-1):
                f.append(1)
            f.append(-1)
        else:
            for _ in range(a-c-1):
                f.append(1)
            f.append(-1)
        table.append(f)
    #print(table)
    cnt=0
    check=True
    while(check):
        #print(table)
        if(cnt>5000):
            print('Case '+str(kase)+': -1')
            kase+=1
            break
        for row in range(n):
            over=over_half(table,cnt)
            if (table[row][cnt]==-1):
                if(over==0):#over
                    print('Case '+str(kase)+': '+str(cnt+1))
                    kase+=1
                    check=False
                    break
                elif(over==1):#can sleep
                    for _ in range(stu[row].r[1]):
                        table[row].append(0)
                    for _ in range(stu[row].r[0]-1):
                        table[row].append(1)
                    table[row].append(-1)
                else:#cannot sleep
                    for _ in range(stu[row].r[0]-1):
                        table[row].append(1)
                    table[row].append(-1)
        cnt+=1
