class Solution:
    def climbStairs(self, n: int) -> int:
        def red(n,m):
            if(n==0):
                return 0
            elif n==1:
                return 1
            elif n==2:
                return 2
            if(str(n) in m):
                return m[str(n)]
            if(str(n-1) in m):
                one = m[str(n-1)]
            else:
                one = red(n-1,m)
                m[str(n-1)]= one
                
            if(str(n-2) in m):
                two = m[str(n-2)]
            else:
                two = red(n-2,m)
                m[str(n-2)]= two
            m[n] = one +two 
            return m[n]
        m= {}
        return red(n,m)
        