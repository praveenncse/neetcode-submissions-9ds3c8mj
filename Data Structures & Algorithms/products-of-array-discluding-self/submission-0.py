class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        emptylist=[]
        
        for i in range(0,len(nums)):
            mul=1
            for j in range(0,len(nums)):
                if i==j:
                    continue
                mul=mul*nums[j]
            emptylist.append(mul)
        return emptylist