class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        
        # Pointers for both strings starting from the end
        i = len(a) - 1
        j = len(b) - 1
        
        # Loop as long as there are digits to process or a carry remains
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
                
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            # The bit to add to our result is total % 2
            result.append(str(total % 2))
            # The new carry is total // 2
            carry = total // 2
            
        # Since we added digits from right to left, reverse the result
        return "".join(reversed(result))
