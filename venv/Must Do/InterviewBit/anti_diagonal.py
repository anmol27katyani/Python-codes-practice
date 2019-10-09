class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n=len(A)
        o=n-1
        h={}
        ans=[]
        for i in range(2*n-1):
            h[i]=[]
        for i in range(n):
            for j in range(n):
                h.setdefault(i+j, []).append(A[i][j])
        for i in range(len(h)):
            ans.append(h[i])
        return(ans)