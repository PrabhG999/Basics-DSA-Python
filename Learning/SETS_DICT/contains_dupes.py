from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

def main():
    # Create an instance of the Solution class
    solution = Solution()

    # Test cases
    nums1 = [1, 2, 3, 1]
    nums2 = [1, 2, 3, 4]
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

    # Call the containsDuplicate method with test cases
    result1 = solution.containsDuplicate(nums1)
    result2 = solution.containsDuplicate(nums2)
    result3 = solution.containsDuplicate(nums3)

    # Print the results
    print(f"Input: {nums1} -> Output: {result1}")  # Expected: True
    print(f"Input: {nums2} -> Output: {result2}")  # Expected: False
    print(f"Input: {nums3} -> Output: {result3}")  # Expected: True


if __name__ == "__main__":
    main()



