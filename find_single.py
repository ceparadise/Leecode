class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        list = []
        for num in nums:
            if num not in list:
                list.append(num)
            else:
                #num_index = list.index(num)
                list.remove(num)
        return list

if __name__ == "__main__":
    e = Solution()
    print e.singleNumber([2,4,5,6,3,4,5])
