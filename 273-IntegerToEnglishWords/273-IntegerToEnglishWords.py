# Last updated: 1/12/2026, 1:41:49 PM
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                    "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                    "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return below_20[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return below_20[n // 100] + " Hundred " + helper(n % 100)

        res = ""
        for i, chunk in enumerate(self.split_by_thousands(num)):
            if chunk > 0:
                res = helper(chunk) + thousands[i] + " " + res

        return res.strip()

    def split_by_thousands(self, num):
        chunks = []
        while num > 0:
            chunks.append(num % 1000)
            num //= 1000
        return chunks
