def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char in count:
            count[char] = count[char] - 1
            if count[char] == 0:
                del count[char]
        else:
            return False
    return len(count) == 0


def main():
    # Test cases
    s1, t1 = "anagram", "nagaram"
    s2, t2 = "rat", "car"

    # Check if t is an anagram of s
    result1 = is_anagram(s1, t1)
    result2 = is_anagram(s2, t2)

    # Print results
    print(f"Input: s = '{s1}', t = '{t1}' -> Output: {result1}")  # Expected: True
    print(f"Input: s = '{s2}', t = '{t2}' -> Output: {result2}")  # Expected: False


if __name__ == "__main__":
    main()
