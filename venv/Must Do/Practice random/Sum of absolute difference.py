"""
Sum of absolute differences of all pairs in a given array
Given a sorted array of distinct elements, the task is to find the summation of absolute differences of all pairs in the given array.

Examples:

Input : arr[] = {1, 2, 3, 4}
Output: 10
Sum of |2-1| + |3-1| + |4-1| +
       |3-2| + |4-2| + |4-3| = 10

Input : arr[] = {1, 8, 9, 15, 16}
Output: 74

Input : arr[] = {1, 2, 3, 4, 5, 7, 9, 11, 14}
Output: 188
"""
def solve(A):
    ans=0
    for i in range(len(A)):
        ans=ans+ (i*A[i]) -(len(A)-i-1)*A[i]
    print(ans)
if __name__=="__main__":
    A=[1, 8, 9, 15, 16]
    solve(A)
