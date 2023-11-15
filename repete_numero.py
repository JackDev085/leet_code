class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return print(set(s) == set(t) and len(set(s)) != len(set(t)))

sol = Solution()

s ="aa"
t ="a"
resultado = sol.isAnagram(s,t)




        