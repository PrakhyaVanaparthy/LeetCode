class Solution:
    def intToRoman(self,a):
        num = int(a)
        dictvalues = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        roman = ''
        
        while num>0:
            for i, k in dictvalues.items():
                if num >= i:
                    div = int(num/i)
                    roman += div*k
                    rem = num%i
                    num = rem
        return roman
