class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f=defaultdict(int)
        for i in range(len(nums)):
            f[nums[i]]+=1

            if f[nums[i]]>1:
                return nums[i]