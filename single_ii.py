class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        dic = {}
        for i in xrange(len(A)):
            if A[i] not in dic:
                dic[A[i]] = 1
            else:
                dic[A[i]] += 1
        for word in dic:
            if dic[word] == 1:
                return word
if __name__ =="__main__":
    e = Solution()
    print e.singleNumber([1,2,3,1,2,1,2])