class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict={}
        for i in xrange(len(num)):
            y = target-num[i]
            if y in dict:
                return dict[y], i+1
            dict[num[i]]= i+1 #把dict[y]=j+1存进了dict里面，直接把index加1然后存成value。然后这样吧y存进去了，之后用
            #target-x=y在不在dict里面来判断。而且，因为y已经在dic里面了，也保证了，y的index是比x小的。

if __name__ == '__main__':
    num = [2,3,4,0,1,5]
    target = 5
    e=Solution().twoSum(num,target)
    print e