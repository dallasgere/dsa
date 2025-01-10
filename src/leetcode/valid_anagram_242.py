"""leetcode problem 242

link: https://leetcode.com/problems/valid-anagram/description/
"""


class ValidAnagram:
    def isAnagram(self, s: str, t: str) -> bool:
        """determines if two strings are valid anagrams

        Args:
            s (str): first string to check
            t (str): second stirng to check

        Returns:
            bool: true if they are valid anagrams, false otherwise
        """
        return sorted(s) == sorted(t)
