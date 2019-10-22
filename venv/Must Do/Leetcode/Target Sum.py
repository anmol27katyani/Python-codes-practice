
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        d = {}
        def dfs(cur, i):
            if i < len(nums) and (i, cur) not in d:
                d[(i, cur)] = dfs(cur + nums[i], i + 1) + dfs(cur - nums[i], i + 1)
            return d.get((i, cur), int(cur == S))
        return dfs(0, 0)