class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
        # hm=set()
        # for i in nums:
        #     if i in hm:
        #         return True
        #     hm.add(i)                          
        # return False
        
        