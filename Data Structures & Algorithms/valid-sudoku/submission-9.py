class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                square = board[r][c]

                if square == ".":
                    continue
                
                if (square in rows[r]
                or square in cols[c]
                or square in squares[(r//3, c//3)]):
                    return False
                
                rows[r].add(square)
                cols[c].add(square)
                squares[(r//3,c//3)].add(square)

        return True