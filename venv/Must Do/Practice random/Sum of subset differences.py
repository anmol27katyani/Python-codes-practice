"""
Given a set S consisting of n numbers, find the sum of difference between last and first element of each subset. We find first and last element of every subset by keeping them in same order as they appear in input set S.

i.e., sumSetDiff(S) = ∑ (last(s) – first(s)),
where sum goes over all subsets s of S.
"""


def SumF(S, n):
    sum = 0
    for i in range(n):
        sum = sum + (S[i] * pow(2, n - i - 1))
    return sum

def SumL(S, n):
    sum = 0
    for i in range(n):
        sum = sum + (S[i] * pow(2, i))
    return sum