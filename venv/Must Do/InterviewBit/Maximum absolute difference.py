class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        a=float('-inf')
        b=float('inf')
        c=float('-inf')
        d=float('inf')
        for i in range(len(A)):
            a=max(a,A[i]+i)
            b=min(b,A[i]+i)
            c=max(c,A[i]-i)
            d=min(d,A[i]-i)
        return max(a - b, c - d)