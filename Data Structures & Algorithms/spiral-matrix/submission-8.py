class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        res = []

        def spiral(left,right,up,down):
            if left > right or up > down:
                return
            
            for i in range(left,right):
                res.append(matrix[up][i])
            
            for i in range(up,down+1):
                res.append(matrix[i][right])
        
            if up < down:
                for i in range(right-1,left,-1):
                    res.append(matrix[down][i])
        
            if left < right:
                for i in range(down,up,-1):
                    res.append(matrix[i][left])

            spiral(left + 1 ,right - 1, up + 1,down - 1)
        spiral(0,m-1,0,n-1)

        return res

