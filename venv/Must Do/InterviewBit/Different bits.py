class Solution:
	# @param A : list of integers
	# @return an integer
	def cntBits(self, A):
        ans = 0
        n=len(A)
        arr=A
        for i in range(0, 32):
            count = 0
            for j in range(0,n):
                if ( (arr[j] & (1 << i)) ):
                    count+=1
            ans += (count * (n - count) * 2)
        return ans