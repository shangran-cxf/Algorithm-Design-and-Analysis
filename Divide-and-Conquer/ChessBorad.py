tile = 1  # L 型骨牌编号


def chessboard(board, top, left, special_row, special_col, size):
    global tile

    # 递归结束：1×1 不需要覆盖
    if size == 1:
        return

    # 当前这一块 L 的编号
    t = tile
    tile += 1

    # 子棋盘大小
    s = size // 2

    # ========= 左上 =========
    if special_row < top + s and special_col < left + s:
        chessboard(board, top, left, special_row, special_col, s)
    else:
        board[top + s - 1][left + s - 1] = t
        chessboard(board, top, left, top + s - 1, left + s - 1, s)

    # ========= 右上 =========
    if special_row < top + s and special_col >= left + s:
        chessboard(board, top, left + s, special_row, special_col, s)
    else:
        board[top + s - 1][left + s] = t
        chessboard(board, top, left + s, top + s - 1, left + s, s)

    # ========= 左下 =========
    if special_row >= top + s and special_col < left + s:
        chessboard(board, top + s, left, special_row, special_col, s)
    else:
        board[top + s][left + s - 1] = t
        chessboard(board, top + s, left, top + s, left + s - 1, s)

    # ========= 右下 =========
    if special_row >= top + s and special_col >= left + s:
        chessboard(board, top + s, left + s, special_row, special_col, s)
    else:
        board[top + s][left + s] = t
        chessboard(board, top + s, left + s, top + s, left + s, s)


# =============================
# 主程序
# =============================
if __name__ == "__main__":
    n = 4  # 必须是 2^n
    board = [[0] * n for _ in range(n)]

    # 特殊格位置
    special_row, special_col = 0, 0
    board[special_row][special_col] = -1

    chessboard(board, 0, 0, special_row, special_col, n)

    for row in board:
        print(row)