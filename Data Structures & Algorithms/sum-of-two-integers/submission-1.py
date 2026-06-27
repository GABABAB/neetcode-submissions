class Solution:
    def getSum(self, a: int, b: int) -> int:
        return a+ b
        carry = (a&b) << 1
        while carry != 0:
            carry = (a&b) << 1
            number = a^b    
            answer = number^carry
        return answer