
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    else:
        return False


def main():
    # Test cases
    nums1 = [1, 2, 3, 1]
    nums2 = [1, 2, 3, 4]
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

    # Check each test case
    result1 = contains_duplicate(nums1)
    result2 = contains_duplicate(nums2)
    result3 = contains_duplicate(nums3)

    # Print results
    print(f"Input: {nums1} -> Output: {result1}")  # Expected: True
    print(f"Input: {nums2} -> Output: {result2}")  # Expected: False
    print(f"Input: {nums3} -> Output: {result3}")  # Expected: True


if __name__ == "__main__":
    main()