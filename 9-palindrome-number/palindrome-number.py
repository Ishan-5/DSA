class Solution:
    def isPalindrome(self, x: int) -> bool:
        text=str(x)
        reverse_text=text[::-1]
        if text == reverse_text:
            return True
        else:
            return False