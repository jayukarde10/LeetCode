class Solution(object):
    def letterCombinations(self, digits):
        
        c={
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        result = [""]

        for i in digits:
            t = []
            for j in result:
                for k in c[i]:
                    t.append(j + k)
            result = t

        return result

         
        """
        :type digits: str
        :rtype: List[str]
        """
        