class Solution:
    def flip(self, A):
        max_diff = 0
        diff = 0
        start = 0
        ans = None
        for i, v in enumerate(A):
            if v=='0':
                diff+=1
            else:
                diff-=1
            if diff < 0:
                diff = 0
                start = i + 1
                continue
            if diff > max_diff:
                max_diff = diff
                ans = [start, i]

        if ans is None:
            return []
        return list(map(lambda x: x + 1, ans))