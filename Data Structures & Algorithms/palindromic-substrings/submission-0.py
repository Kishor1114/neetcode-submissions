class Solution:
    def countSubstrings(self, s: str) -> int:
        def expandAroundCenter(left: int, right: int) -> int:
            count = 0
            # Expand around the center while the characters at both ends are equal.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count

        if not s:
            return 0

        total_palindromes = 0

        for i in range(len(s)):
            # Check for odd-length palindromes.
            total_palindromes += expandAroundCenter(i, i)

            # Check for even-length palindromes.
            total_palindromes += expandAroundCenter(i, i + 1)

        return total_palindromes