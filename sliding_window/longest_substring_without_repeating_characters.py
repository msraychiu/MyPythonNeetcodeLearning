class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            hash_set = set()
            length = 0
            i = 0
            for char in s:
                while char in hash_set:
                    hash_set.remove(s[i])
                    i += 1
                hash_set.add(char)
                length = max(length, len(hash_set))
            return length