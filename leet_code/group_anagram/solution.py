from typing import List

# https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result: dict[tuple, List] = {}
        for str in strs:
            char_array = list(str)
            char_array.sort()
            key = tuple(char_array)

            if key in result.keys():
                result[key].append(str)
            else:
                result[key] = [str]
        return list(result.values())
