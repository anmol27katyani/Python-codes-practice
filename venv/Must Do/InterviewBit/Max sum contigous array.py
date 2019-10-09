class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_so_far=A[0]
        max_ending_here=float('-inf')
        for i in range(len(A)):
            max_ending_here=max(max_ending_here+A[i],A[i])
            if max_so_far<max_ending_here:
                max_so_far=max_ending_here
        return max_so_far