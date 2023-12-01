def hexx(n):
    s=0
    a=len(n)
    for i in range(a):
        if n[i]=='a':
            s+=10*16**(a-i-1)
        elif n[i]=='b':
            s+=11*16**(a-i-1)
        elif n[i]=='c':
            s+=12*16**(a-i-1)
        elif n[i]=='d':
            s+=13*16**(a-i-1)
        elif n[i]=='e':
            s+=14*16**(a-i-1)
        elif n[i]=='f':
            s+=15*16**(a-i-1)
        else:
            s+=int(n[i])*16**(a-i-1)
    return s
def SelectionSort(a,b):
    for i in range(0,len(a)-1):
        ind_max=i
        for j in range(i+1, len(a)):
            if a[j]<a[ind_max]:
                ind_max=j
        a[i], a[ind_max] = a[ind_max], a[i]
        b[i],b[ind_max]=b[ind_max],b[i]
    return b
s0=[]
su=[]

with open('out.csv') as f:
    for line in f.readlines():
        s=line.strip().split(',')
        s0.append(hexx(s[-1][1:]))
        su.append(s)
        

n_su=SelectionSort(s0,su)
import csv
with open('new.csv', 'w', newline='') as csvfile:
    filewriter=csv.writer(csvfile, delimiter=',',
    quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for x in range(len(n_su)):
        filewriter.writerow(n_su[x]) 
