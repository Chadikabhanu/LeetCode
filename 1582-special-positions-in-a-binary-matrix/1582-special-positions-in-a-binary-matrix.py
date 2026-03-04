class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m=len(mat)
        n=len(mat[0])
        rowcount=[0] * m
        colcount=[0] * n
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    rowcount[i]+=1
                    colcount[j]+=1
        special=0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and rowcount[i] == 1 and colcount[j] == 1:
                    special+=1
        return special
