class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            return False

        freq = Counter(hand)
        for _ in range(n//groupSize):
            min_element = min(freq)
            for j in range(min_element, min_element + groupSize):
                if j not in freq:
                    return False
                freq[j] -= 1
                if freq[j] <= 0:
                    del freq[j]
                

        return True
                    