class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict={}
        for i,x in enumerate(num):
           dict[x]=i
        for x in num:
            y = target-x
            if y in num:
                i = dict[x]
                j = dict[y]
                return i, j
if __name__ == '__main__':
    num = [2,3,4,0,1,5]
    target = 5
    e=Solution().twoSum(num,target)
    print e