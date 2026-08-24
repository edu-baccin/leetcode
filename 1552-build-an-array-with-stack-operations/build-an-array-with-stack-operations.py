class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s = []
        result = []
        check = 1
        while s != target:
            if target.count(check) == 1:
                result.append("Push")
                s.append(check)
            if target.count(check) == 0:
                result.append("Push")
                result.append("Pop")
            check += 1
        return result          
