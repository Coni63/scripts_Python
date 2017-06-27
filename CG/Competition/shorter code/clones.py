z={}
a,b,c,d,e,f,g,h=[int(i) for i in input().split()]
for i in range(h):
    i,k=[int(j) for j in input().split()]
    z[i]=k
z[d]=e
while True:
    l,m,o=input().split()
    l=int(l);m=int(m)
    try:
        if (m>z[l] and o=="RIGHT") or (m<z[l] and o=="LEFT"):print("BLOCK")
        else:print("WAIT")
    except:
        print("WAIT")