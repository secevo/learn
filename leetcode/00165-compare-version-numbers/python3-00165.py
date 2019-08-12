class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list1 = list(map(int, version1.split('.')))
        list2 = list(map(int, version2.split('.')))
        max_len = max(len(list1), len(list2))
        for i in range(max_len):
            v1 = list1[i] if i < len(list1) else 0
            v2 = list2[i] if i < len(list2) else 0
            if v1 < v2:
                return -1
            if v1 > v2:
                return 1
        return 0