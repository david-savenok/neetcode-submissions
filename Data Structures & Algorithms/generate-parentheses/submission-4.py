class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []

        def _generatePar(s, o_par, c_par):
            if c_par - o_par < 0:
                _generatePar(s + ')', o_par, c_par + 1)
            if o_par < n:
                _generatePar(s + '(', o_par + 1, c_par)
            if o_par == c_par == n:
                self.res.append(s) 
        
        _generatePar('', 0, 0)
        return self.res



        