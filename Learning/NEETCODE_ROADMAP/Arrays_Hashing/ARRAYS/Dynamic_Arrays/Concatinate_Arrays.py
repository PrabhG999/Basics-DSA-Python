from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """""ans = []
        for num in nums:
            ans.append(num)
        ans +=nums
        return ans"""""
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans


def main():
    # Create an instance of the Solution class
    solution = Solution()

    # List to concatenate
    nums = [1, 2, 3]

    # Call the getConcatenation method
    result = solution.getConcatenation(nums)

    # Print the result
    print("Original list:", nums)
    print("Concatenated list:", result)


if __name__ == "__main__":
    main()
