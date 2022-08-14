class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = {}
        res = 0
        i = 0
        for j in range(len(s)):
            map[s[j]] = map.get(s[j], 0) + 1

            if (j - i + 1) - max(map.values()) > k:
                map[s[i]] = map[s[i]] - 1
                i += 1

            res = max(res, j - i + 1)

        return res




