"""leetcode problem 49

link: https://leetcode.com/problems/group-anagrams/description/
"""


class GroupAnagrams:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """groups strings in list into anagram groups

        Args:
            strs (list[str]): the strings to sort through

        Returns:
            list[list[str]]: the returned list of anagrams grouped together
        """
        groups: dict[str, list[str]] = {}
        self.get_groups(groups, strs)
        for s in strs:
            sorted_s = "".join(sorted(s))
            groups[sorted_s].append(s)

        return list(groups.values())

    def get_groups(self, groups: dict[str, list[str]], strs: list[str]) -> None:
        """Gets the groups for the group anagrams method.
        I broke out this method because it is easier conceptually then keeping them all together.

        Args:
            groups (dict[str, list[str]]): the groups to populate, uses references so no return value needed
            strs (list[str]): the list of strings to aquire the groups from
        """
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in groups:
                groups[sorted_s] = []
