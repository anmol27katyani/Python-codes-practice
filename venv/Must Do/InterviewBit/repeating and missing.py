class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        A = list(A)
        p = 0
        m = 0
        for i in range(len(A)):
            if (A[abs(A[i]) - 1]) > 0:
                A[abs(A[i]) - 1] = -A[abs(A[i]) - 1]
            else:
                p = abs(A[i])

        for i in range(len(A)):
            if A[i] > 0:
                m = i + 1

        return [p, m]