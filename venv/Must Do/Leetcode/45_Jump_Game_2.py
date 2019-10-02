class Solution:
    def jump(self, nums: List[int]) -> int:
        ln = len(nums)
        if ln <= 1:
            return 0

        cnt = till = 0
        maxIdx = 0
        for i in range(ln):
            maxIdx = max(maxIdx, i + nums[i])
            if i == till:
                cnt += 1
                till = maxIdx
            if till >= ln - 1:
                return cnt