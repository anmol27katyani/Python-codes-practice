class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if not list1 or not list2: return []
        d = {}
        res = (math.inf)
        for i in range(len(list1)):
            d[list1[i]] = d.get(list1[i], []) + [i]
        for i in range(len(list2)):
            d[list2[i]] = d.get(list2[i], []) + [i]
        for i in d:
            if len(d[i]) == 2:
                sm = sum(d[i])
                if sm < res:
                    res = sm
                    res1 = [i]
                elif sm == res:
                    res1.append(i)
        return res1
