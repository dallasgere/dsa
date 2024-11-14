"""
leetcode problem 125
"""


class ValidPalindrom:
    def isPalindrome(self, s: str) -> bool:
        """determines if string is palindrome

        Args:
            s (str): string to look check

        Returns:
            bool: True if palindrome, False otherwise
        """
        clean = "".join([char.lower() for char in s if char.isalnum()])
        return clean == clean[::-1]
