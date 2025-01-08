"""
水仙花数
要求输出m到n范围内的水仙花数
"""

class Solution():
    def __init__(self, m, n):
        self.m = m
        self.n = n

    def generate(self):
        result = []
        for num in range(self.m, self.n + 1):
            if self.is_sxh(num):
                result.append(num)
        return result

    def is_sxh(self, num):
        digits = str(num)
        if len(digits) != 3:
            return False
        d_0 = int(digits[0])
        d_1 = int(digits[1])
        d_2 = int(digits[2])
        num_r = d_0**3 + d_1**3 + d_2**3
        return num == num_r

    def output(self):
        result = self.generate()
        if result:
            print(' '.join(map(str, result)))
        else:
            print("no")

if __name__ == '__main__':
    while True:
        try:
            m, n = map(int, input().split())
            solution = Solution(m, n)
            solution.output()
        except EOFError:
            break