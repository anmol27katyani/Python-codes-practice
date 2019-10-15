"""
Minimum sum of differences with an element in an array
Given an array, we need to find the sum of elements of an array after changing the element as arr[i] will become abs(arr[i]-x) where x is an array element.

Examples:

Input  : {2, 5, 1, 7, 4}
Output : 9
"""
def absSumDidd(a, n):
    a.sort()
    midValue = a[(int)(n // 2)]
    sum = 0
    for i in range(n):
        sum = sum + abs(a[i] - midValue)
    return sum
arr = [5, 11, 14, 10, 17, 15]
n = len(arr)
print(absSumDidd(arr, n))