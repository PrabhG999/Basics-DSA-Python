from collections import defaultdict
from typing import List


def group_anagrams( strs: List[str]) -> List[List[str]]:
    anagram = defaultdict(list)

    for e_w in strs:
        sorted_key = tuple(sorted(e_w))
        anagram[sorted_key].append(e_w)
    return list(anagram.values())


def main():
    # Test cases
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs2 = [""]
    strs3 = ["a"]

    # Run group_anagrams on each test case
    result1 = group_anagrams(strs1)
    result2 = group_anagrams(strs2)
    result3 = group_anagrams(strs3)

    # Print the results
    print(f"Input: strs = {strs1} -> Output: {result1}")
    print(f"Input: strs = {strs2} -> Output: {result2}")
    print(f"Input: strs = {strs3} -> Output: {result3}")


if __name__ == "__main__":
    main()
