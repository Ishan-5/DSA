class Solution:
    def numberToWords(self, num: int) -> str:
        # Edge Case
        if num == 0:
            return "Zero"
            
        # 1. Map out all English word constants
        LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        THOUSANDS = ["", "Thousand", "Million", "Billion"]
        
        # 2. Helper function to process groups of 3 digits (numbers under 1000)
        def helper(n):
            if n == 0:
                return []
            elif n < 20:
                return [LESS_THAN_20[n]]
            elif n < 100:
                return [TENS[n // 10]] + helper(n % 10)
            else:
                return [LESS_THAN_20[n // 100], "Hundred"] + helper(n % 100)
        
        res = []
        i = 0
        
        # 3. Process the number in blocks of 3 digits from right to left
        while num > 0:
            if num % 1000 != 0:
                # Get the words for the 3-digit block and add the suffix (Thousand, Million, etc.)
                res = helper(num % 1000) + [THOUSANDS[i]] + res
            num //= 1000
            i += 1
            
        # 4. Join words with spaces, cleaning up any empty strings from the helper recursion
        return " ".join([word for word in res if word])
