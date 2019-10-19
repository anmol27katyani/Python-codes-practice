class Solution(object):
    def findPairs(self, nums, k):
        nums.sort()
        count = []
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                count.append((dict[nums[i]],nums[i]))
            dict[nums[i]+k] = nums[i]
        return len(set(count))