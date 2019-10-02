t=int(input())
for _ in range(t):
    n=int(input())
    g=[[] for i in range(2*n)]
    gg=[[] for i in range(2*n)]
    arr=list(map(int,input().split()))
    for ii in range(n-1):
        x,y=map(int,input().split())
        g[x].append(arr[y - 1])
        gg[x].append(y)
        g[y].append(arr[x-1])
        gg[y].append(x)
    ans=[0]*(n+1)
    for i in range(n):
        ans[i]=sum(g[i+1])+arr[i]
    x=n
    fin=[0]*(n+5)
    anmol=0
    while(x>0):
        temp=(ans.index(max(ans)))+1
        if temp>n:
            anmol=0
            break
        if arr[temp]<0:
            ans[temp]=-2
        anmol+=ans[temp-1]
        ans[temp-1]=0
        fin[temp]=temp
        for i in (gg[temp]):
            fin[i]=i
            ans[i-1]=0
        x=x-len(gg[temp])-1
    if anmol==-1:
        print("Case #",end="")
        print(_+1,end="")
        print(": ",end="")
        print(0)
    else:
        print("Case #",end="")
        print(_+1,end="")
        print(": ",end="")
        print(anmol)
