__author__ = 'vivian'
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        one = 0
        for num in nums:
            one = one ^ num
        return one

if __name__ == "__main__":
    e = Solution()
    print e.singleNumber([2,1,4,2,1])


    #xor的定义，是在bit上比较是否相同，不同反1，相同返0.所以，0和任何数的xor都是那个数。任何数a 和 数b xor两次数b，都是a