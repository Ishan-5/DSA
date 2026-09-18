class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        clean_s = "".join(char.lower() for char in s if char.isalnum())
        reverse_s = clean_s[::-1]
        return clean_s==reverse_s

