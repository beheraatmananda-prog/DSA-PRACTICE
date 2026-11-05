class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_1 = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in dict_1:
                dict_1[key].append(s)
            else:
                dict_1[key] = [s]
        return list(dict_1.values())