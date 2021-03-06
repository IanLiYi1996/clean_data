import os,sys
from typing import List

def search(L: int, a: int, modulus: int, n: int, nums: List[int]) -> int:
    """
    Rabin-Karp with polynomial rolling hash.Search a substring of given length that occurs at least 2 times.
    @return start position if the substring exits and -1 otherwise.
    """
    h = 0
    for i in range(L):
        h = (h * a + nums[i]) % modulus
    # already seen hashes of strings of length L
    seen = {h}
    # const value to be used often : a**L % modulus
    aL = pow(a, L, modulus)
    for start in range(1, n - L + 1):
        # compute rolling hash in O(1) time
        h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % modulus
        if h in seen:
            return start
        seen.add(h)
    return -1


def longestDupSubstring(S: str) -> str:
    n = len(S)
    nums = [ord(S[i]) - ord('a') for i in range(n)]
    a = 26
    # modulus value for the rolling hash function to avoid overflow
    modulus = 2 ** 32
    # binary search, L = repeating string length
    left, right = 1, n
    while left != right:
        L = left + (right - left) // 2
        if search(L, a, modulus, n, nums) != -1:
            left = L + 1
        else:
            right = L

    start = search(left - 1, a, modulus, n, nums)
    return S[start: start + left - 1] if start != -1 else ""

def replace_space(S: str) -> str:
    pass


if __name__ == '__main__':
    result = longestDupSubstring("abcabc")
    print(result)