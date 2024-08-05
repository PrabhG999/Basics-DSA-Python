from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        maps = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in maps:
                return [maps[comp], i]
            maps[num] = i
        return []


def main():
    # Create an instance of the Solution class
    solution = Solution()

    # Test cases
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    print(f"Input: nums = {nums1}, target = {target1} -> Output: {result1}")  # Expected: [0, 1]

    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print(f"Input: nums = {nums2}, target = {target2} -> Output: {result2}")  # Expected: [1, 2]

    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    print(f"Input: nums = {nums3}, target = {target3} -> Output: {result3}")  # Expected: [0, 1]


if __name__ == "__main__":
    main()
