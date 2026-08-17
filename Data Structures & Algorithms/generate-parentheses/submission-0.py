class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []

        def _generatePar(s, o_par, c_par, remaining):
            if c_par - o_par < 0:
                _generatePar(s + ')', o_par, c_par + 1, remaining)
                if remaining > 0:
                    _generatePar(s + '(', o_par + 1, c_par, remaining - 1)
            elif c_par - o_par == 0 and remaining > 0:
                _generatePar(s + '(', o_par + 1, c_par, remaining - 1)
            else:
                self.res.append(s) 
        
        _generatePar('', 0, 0, n)
        return self.res



        