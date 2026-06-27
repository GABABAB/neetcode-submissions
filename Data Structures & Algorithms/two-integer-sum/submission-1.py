class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for position, number in enumerate(nums):
            search = target - number
            if search in seen:
                return [seen[search], position]
            else:
                seen.update({number: position})
        