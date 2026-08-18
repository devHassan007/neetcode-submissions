class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices={}
        i=0
        for n in nums:
            diff=target-nums[i]
            if diff in indices:
                return [indices[diff], i]
                break
            else:
                indices[nums[i]]=i
            i=i+1
        