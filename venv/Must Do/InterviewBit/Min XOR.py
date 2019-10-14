class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        A=sorted(A)
        ans=0
        for i in range(len(A)-1):
            t=A[i]^A[i+1]
            if t<ans:
                t=ans
        return ans
