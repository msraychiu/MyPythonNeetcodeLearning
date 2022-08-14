class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        map1 = {}
        map2 = {}
        for x in s1:
            map1[x] = map1.get(x, 0) + 1

        for y in range(len(s1)):
            map2[s2[y]] = map2.get(s2[y], 0) + 1
        if map1 == map2: return True

        for z in range(len(s2)):
            if map1 == map2:
                return True
            elif z > 0 and z+len(s1) <= len(s2):
                map2[s2[z-1]] = map2[s2[z-1]] - 1
                if map2[s2[z-1]] <= 0:
                    map2.pop(s2[z-1])

                map2[s2[z+len(s1)-1]] = map2.get(s2[z+len(s1)-1], 0) + 1

        return False