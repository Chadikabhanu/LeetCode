class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=set()
        cols=set()
        boxs=set()
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                rows_key=(row,num)
                cols_key=(col,num)
                boxs_key=((row//3,col // 3),num)
                if rows_key in rows or cols_key in cols or boxs_key in boxs:
                    return False
                rows.add(rows_key)
                cols.add(cols_key)
                boxs.add(boxs_key)
        return True