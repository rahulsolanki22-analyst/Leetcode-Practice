class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sort = sorted(nums)
        d = {}
        for i in range(len(sort)):
            if sort[i] not in d:
                d[sort[i]]=i
        ret = []
        for i in nums:
            ret.append(d[i])
        return ret