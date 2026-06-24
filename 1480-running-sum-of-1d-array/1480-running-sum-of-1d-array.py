class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            l.append(total)
        return l