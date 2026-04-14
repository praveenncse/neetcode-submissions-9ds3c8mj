class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(0,len(nums)):
            for k in range(i+1,len(nums)):
                if nums[i]==nums[k]:
                    return True

        return False
            
                