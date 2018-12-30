import numpy as np
class Solution(object):
    def twoSum(self, nums, target):
        num_dict=dict(zip(nums,range(len(nums))))
        #return list(num_dict.keys()),list(num_dict.values())
        for i in range(len(nums)):
            if num_dict.has_key(target-nums[i]) and i!=num_dict[target-nums[i]]:
                return [i,num_dict[target-nums[i]]]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
