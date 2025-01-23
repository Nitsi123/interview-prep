class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}
        for i, num in enumerate(nums):
            dict[num] = i
        res = []
        for i, num in enumerate(nums):
            comp = target - num
            if comp in dict and i != dict[comp]:
                res.append(i)
                res.append(dict[comp])
                break
        
        return res
        