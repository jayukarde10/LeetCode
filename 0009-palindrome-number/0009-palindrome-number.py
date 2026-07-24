class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y=str(x)
        left=0
        right=len(y)-1
        while left<right:
            if(y[left]==y[right]):
                left+=1
                right-=1
            else:
                return False
        else:
            return True
        