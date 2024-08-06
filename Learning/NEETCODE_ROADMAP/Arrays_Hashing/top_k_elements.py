from typing import List
from collections import defaultdict


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    freq_map = defaultdict(int)
    # count and add the frequency of each value in the map as element:frequency
    for num in nums:
        freq_map[num] += 1

    # convert frequency map to a list where it comes out in desending order
    freq_list = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

    top_k_elements = [element for element,frequency in freq_list[:k]]

    return top_k_elements


def main():
    # Test cases
    nums1, k1 = [1, 1, 1, 2, 2, 3], 2
    nums2, k2 = [1], 1

    # Run top_k_frequent on each test case
    result1 = top_k_frequent(nums1, k1)
    result2 = top_k_frequent(nums2, k2)

    # Print the results
    print(f"Input: nums = {nums1}, k = {k1} -> Output: {result1}")  # Expected: [1, 2]
    print(f"Input: nums = {nums2}, k = {k2} -> Output: {result2}")  # Expected: [1]


if __name__ == "__main__":
    main()
