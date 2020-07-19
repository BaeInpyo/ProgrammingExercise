class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '0':
            return b
        if b == '0':
            return a
        
        carry = 0
        a_idx = len(a) - 1
        b_idx = len(b) - 1
        result = ''
        while a_idx >= 0 or b_idx >= 0:
            x = carry
            if a_idx >= 0 and a[a_idx] == '1':
                x += 1
            
            if b_idx >= 0 and b[b_idx] == '1':
                x += 1
            
            carry = x // 2
            x %= 2
            a_idx -= 1
            b_idx -= 1
            
            result = '1' + result if x else '0' + result
        if carry:
            result = '1' + result
            
        return result if result[0] == '1' else result[1:]
