class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subGridSet = [set(), set(), set()]
        rowSet = set()
        nineColumns = [set() for _ in range(9)] 
        subGrid = 0
        subGridRowCounter = 0

        subGridSetCount = [0,0,0]
        rowSetCount = 0
        nineColumnsCount = [0] * 9


        for row in range(len(board)):

            if (row % 3 == 0):
                for i in range(len(subGridSet)):
                    # print(f"(Row: {row}) {sub}")
                    subGridSet[i].clear()
                    subGridSetCount[i] = 0

            for column in range(len(board)):
                
                if (column % 3 == 0) and (column > 0):
                    subGrid+=1

                value = board[row][column]
                if value == '.':
                    continue
                
                rowSet.add(value)
                nineColumns[column].add(value)
                subGridSet[subGrid].add(value)

                # print(f"Column {column}: {nineColumns[column]}")

                if nineColumnsCount[column] == len(nineColumns[column]):
                    return False
                else:
                    # print(nineColumns[column])
                    nineColumnsCount[column] = len(nineColumns[column])
                if rowSetCount == len(rowSet):
                    return False
                else:
                    # print(rowSet)
                    rowSetCount = len(rowSet)
                if subGridSetCount[subGrid] == len(subGridSet[subGrid]):
                    return False
                else:
                    # print(subGridSet[subGrid])
                    subGridSetCount[subGrid] = len(subGridSet[subGrid])

            print(f"Row {row}: {rowSet}")
            rowSet.clear()
            rowSetCount = 0
            subGrid = 0
            
        return True


