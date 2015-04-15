class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict={}
        for i in xrange(len(num)):
            y = target-num[i]
            if y in dict:
                return dict[y], i+1
            dict[num[i]]= i+1

if __name__ == '__main__':
    num = [2,3,4,0,1,5]
    target = 5
    e=Solution().twoSum(num,target)
    print e