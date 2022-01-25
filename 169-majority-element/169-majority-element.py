class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        tmp = None
        for i in nums:
            if count == 0:
                tmp = i
            count += (1 if i == tmp else -1)
            
        return tmp