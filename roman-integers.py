class Solution:
    def romanToInt(self, s: str) -> int:
        sum=0
        romans = {
          "I": 1,
          "V": 5,
          "X": 10,
          "L": 50,
          "C": 100,
          "D": 500,
          "M": 1000
        }
        for i in range(0,len(s)-1):
            if romans[s[i]]>=romans[s[i+1]]:
                sum=sum+romans[s[i]]
            else:
                sum=sum-romans[s[i]]
        sum=sum+romans[s[len(s)-1]]
        return sum