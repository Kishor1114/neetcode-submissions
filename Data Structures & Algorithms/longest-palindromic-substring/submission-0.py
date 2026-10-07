class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> str:
            # Expand around the center while the characters at both ends are equal.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome substring.
            return s[left + 1 : right]

        if len(s) < 2:
            return s

        longest = ""

        for i in range(len(s)):
            # Check for odd-length palindromes.
            palindrome1 = expandAroundCenter(i, i)
            if len(palindrome1) > len(longest):
                longest = palindrome1

            # Check for even-length palindromes.
            palindrome2 = expandAroundCenter(i, i + 1)
            if len(palindrome2) > len(longest):
                longest = palindrome2

        return longest