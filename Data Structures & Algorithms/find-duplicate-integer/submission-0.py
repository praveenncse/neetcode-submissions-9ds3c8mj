class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f=defaultdict(int)
        for i in range(len(nums)):
            f[nums[i]]+=1

        for key,values in f.items():
            if values>1:
                return key
