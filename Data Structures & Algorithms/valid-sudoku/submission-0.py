class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_set = collections.defaultdict(set)
        cols_set = collections.defaultdict(set)
        boxes_set = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                element = board[r][c]

                if element == '.': continue

                if element in rows_set[r]:
                    return False

                if element in cols_set[c]:
                    return False

                boxR = r // 3
                boxC = c // 3

                if element in boxes_set[(boxR, boxC)]:
                    return False
                
                rows_set[r].add(element)
                cols_set[c].add(element)
                boxes_set[((boxR, boxC))].add(element)

        return True
 