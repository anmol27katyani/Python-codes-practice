t=int(input())
for _ in range(t):
    n,s=map(int,input().split())
    c=[]
    for ki in range(n):
        arr = list(map(int, input().split()))
        arr=arr[1:]
        c.append(arr)
    ans=0
    flag=0
    for i in range(len(c)):
        for j in range(i+1,len(c)):
            x=(c[i]+c[j])
            if sorted(c[i])==sorted(c[j]):
                flag+=1
            x=sorted(x)
            for k in range(len(x)-1):
                if x[k+1]!=x[k]:
                    ans+=1
                    break
    print("Case #",end="")
    print(_+1,end="")
    print(": ",end="")
    if flag==n:
        print(0)
    else:
        print(ans + 1)
