class Solution:
    #yalin@return an integer
    def reverse(self,x):
        if x < 0:
            sign = -1
        elif x >= 0 :
            sign = 1
        result = sign * int(str(abs(x))[::-1])
        if result > 2147483648 or result < -2147483648:
            return 0
        else:
            return result

if __name__ == '__main__':
    x = 1534236469
    print Solution().reverse(x)
