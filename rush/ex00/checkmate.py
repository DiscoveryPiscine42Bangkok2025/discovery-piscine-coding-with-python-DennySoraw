def checkmate(board: str):
    board = [list(row) for row in board.strip().split('\n')]
    if not board: # เช็คว่าเป็นกระดานเปล่ามั้ย
        print("Fail")
        return
    
    size = len(board)
    king_index = None

    for i in range(size):    # หาตำแหน่ง king
        for j in range(size):
            if board[i][j] == 'K':
                king_index = (i, j)
                break
        if king_index:
            break

    if not king_index:  # ถ้าไม่พบ king ในกระดาน
        print("Fail")
        return
    
    king_row, king_column = king_index

    def check_direction(start_row, start_column, dir_row, dir_column):
        row, column = start_row + dir_row, start_column + dir_column
        while 0 <= row < size and 0 <= column < size:
            if row == king_row and column == king_column:   # พบการโจมตี king
                return True
            if board[row][column] != ' ':   # direction ถูกบังด้วยหมากตัวอื่น
                return False
            row += dir_row
            column += dir_column
        return False
    

    for i in range(size): # check หมากทุกตัวบนกระดาน
        for j in range(size):
            piece = board[i][j]

            if piece == 'P': # แนวทแยงด้านหน้า
                if (i - 1 == king_row and j - 1 == king_column) or (i - 1 == king_row and j + 1 == king_column):
                    print("Success")
                    return
            elif piece == 'R' or piece == 'Q': # แนวตั้งและแนวนอน
                if check_direction(i, j, 0, 1) or \
                    check_direction(i, j, 0, -1) or \
                    check_direction(i, j, 1, 0) or \
                    check_direction(i, j, -1, 0):
                        print("Success")
                        return

            if piece == 'B' or piece == 'Q': # แนวทแยง
                if check_direction(i, j, 1, 1) or \
                    check_direction(i, j, 1, -1) or \
                    check_direction(i, j, -1, 1) or \
                    check_direction(i, j, -1, -1):
                        print("Success")
                        return
    print("Fail") # ถ้าไม่พบการโจมตี

