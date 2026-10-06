class Solution:
    def twoSum(self, nums,target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

s1 = Solution()
nums = [2,7,11,15]
target = 9
result = s1.twoSum(nums, target)
print(result)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []

