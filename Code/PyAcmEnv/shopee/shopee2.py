class Solution:

    def is_palindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    def valid_palindrome(self, s) :
        # write code here
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.is_palindrome(s[left + 1: right + 1]) or self.is_palindrome(s[left: right])
            left += 1
            right -=1

        return True

if __name__ == '__main__':
    s = input()
    solution = Solution()
    print(solution.valid_palindrome(s))
