a,b,x,y=list(map(int,input().split()))
while True:
    d=""
    if b>y:d="S";y+=1
    if b<y:d="N";y-=1
    if a>x:d+="E";x+=1
    if a<x:d+="W";x-=1
    print(d) 