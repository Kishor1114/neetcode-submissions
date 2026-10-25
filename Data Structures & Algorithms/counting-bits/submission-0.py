class Solution:
    def countBits(self, num: int) -> List[int]:
        bits_count = [0] * (num + 1)

        for i in range(1, num + 1):
            bits_count[i] = bits_count[i // 2] + (i % 2)

        return bits_count