from collections import deque
t=int(input())
for ii in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    i = 0
    j = 1
    ssf=a[0]
    s = k
    a.append(0)
    while  (i < n) and (j <= n):
        if ssf<s:
            ssf += a[j]
            j += 1
        elif ssf>s:
            ssf-=a[i]
            i+=1
        elif ssf==s:
            break
    if j>n or i+1>n:
        print(-1)
    else:
        print(i+1,j)