class Solution(object):
    def isValid(self, s):
        t=[]
        c={
            "(":")",
            "[":"]",
            "{":"}"
        }
        ct=["(","{","["]
        for i in s:
            if i in ct:
                t.append(i)
            else:
                if t==[]:
                    return False
                top=t.pop()
                if c[top]!=i:
                    return False
                
        return t==[]
        """
        :type s: str
        :rtype: bool
        """
        