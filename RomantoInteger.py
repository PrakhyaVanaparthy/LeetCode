class Solution(object):
    def romanToInt(self, s):
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        curr = 0
        prev = 0
        total = 0

        for i in range(len(s)):
            curr = dict[s[i]]
            if curr > prev:
                total = total + curr - 2 * prev
            else:
                total = total + curr
            prev = curr
        return total
