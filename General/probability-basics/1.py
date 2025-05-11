# How many ways are there to permute the letters in the word MISSISSIPPI?

class Solution:
    def __init__(self, input_string: str):
        self.input_string = input_string
        self.result_set = []

    def simulate(self, current_string: str, remaining_chars: list[str]):
        if not remaining_chars:
            self.result_set.append(current_string)
            return

        for i in range(len(remaining_chars)):
            new_remaining_chars = remaining_chars[:i] + remaining_chars[i+1:]
            self.simulate(current_string + remaining_chars[i], new_remaining_chars)

    def get_permutations(self):
        self.simulate("", list(self.input_string))
        return self.result_set

# Example usage:
word = "MISSISSIPPI"
solution = Solution(word)
permutations = solution.get_permutations()
result = len(permutations)
print(result)

