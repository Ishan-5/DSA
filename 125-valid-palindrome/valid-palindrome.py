class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        clean_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        reverse_s = clean_s[::-1]
        return clean_s==reverse_s

