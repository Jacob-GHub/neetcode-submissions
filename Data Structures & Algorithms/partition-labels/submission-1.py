class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        last_index = {}
        for i, char in enumerate(s):
            last_index[char] = i

        i = 0
        res = []
        while i < n:
            next_start = last_index[s[i]]
            j = i
            while j < next_start + 1:
                next_start = max(next_start, last_index[s[j]])
                j+=1
            res.append(next_start - i + 1)
            i = next_start + 1
        
        return res


