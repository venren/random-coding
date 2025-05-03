# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# Order of complexity - O(n)

class Solution:
    def twoSums(self, input:list, target: int):
        indexMap = {}
        for ind, i in enumerate(input):
            indexMap[i] = ind

        for k in indexMap:
            test = target - k
            if test in indexMap:
                return([indexMap[k], indexMap[test]])
        
        return[-1,-1]
    
sol= Solution()
result = sol.twoSums([2,7,11,15], 9)
print(result)





        