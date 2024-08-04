def two_sum(nums, target):
    map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in map:
            return [map[complement], i]
        map[num] = i
    return []


def main():
    # Test cases
    nums1, target1 = [2, 7, 11, 15], 9
    nums2, target2 = [3, 2, 4], 6
    nums3, target3 = [3, 3], 6

    # Run two_sum on each test case
    result1 = two_sum(nums1, target1)
    result2 = two_sum(nums2, target2)
    result3 = two_sum(nums3, target3)

    # Print the results
    print(f"Input: nums = {nums1}, target = {target1} -> Output: {result1}")  # Expected: [0, 1]
    print(f"Input: nums = {nums2}, target = {target2} -> Output: {result2}")  # Expected: [1, 2]
    print(f"Input: nums = {nums3}, target = {target3} -> Output: {result3}")  # Expected: [0, 1]


if __name__ == "__main__":
    main()
