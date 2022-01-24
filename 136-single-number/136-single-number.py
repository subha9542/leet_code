class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_ = defaultdict(int)
        for i in nums:
            hash_[i] += 1
            
        for i in hash_:
            if(hash_[i] == 1):
                return i