class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        p=[]
        for i in range(A+1):
            p.append([1]*(i+1))
        for i in range(A+1):
            p[i][0] = 1
            p[i][i] = 1
            for j in range(1, i):
                p[i][j] = p[i-1][j-1] + p[i-1][j]
        return p[A]