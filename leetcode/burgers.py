import numpy as np
import sklearn
# Given tomatoSlices and cheeseSlices, find total_jumbo and total_small burgers
# such that 4*total_jumbo + 2*total_small = tomatoSlices and total_jumbo + total_small = cheeseSlices.
# Return [total_jumbo, total_small] if possible, otherwise return [].

# Input: tomatoSlices = 16, cheeseSlices = 7
# Output: [1,6]
# Explantion: To make one jumbo burger and 6 small burgers we need 4*1 + 2*6 = 16 tomato and 1 + 6 = 7 cheese.
# There will be no remaining ingredients.

# Input: tomatoSlices = 17, cheeseSlices = 4
# Output: []

# Input: tomatoSlices = 4, cheeseSlices = 17
# Output: []

class Solution:
    def burger(self, tomato: int, cheese: int):
        result = np.array([tomato, cheese])
        input = np.array([[4,2],[1,1]])
        model = sklearn.linear_model.LinearRegression(fit_intercept=False)
        model.fit( input, result)
        jumbo, small = model.coef_
        jumbo = round(jumbo,2)
        small = round(small,2)

        if jumbo.is_integer() and small.is_integer() and jumbo >=0 and small >= 0 :
            return[jumbo, small]

        return []


sol = Solution()
result = sol.burger(100, 30)
print(result)