class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while s and t > s[-1][0]:
                st, si = s.pop()
                res[si] = i - si
            s.append((t, i))

        return res

