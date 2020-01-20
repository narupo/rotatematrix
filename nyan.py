import sys


# 操作対象の行列
mat = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]


def create_zero_matrix(nrow, ncol):
    """
    nrow x ncolの零行列を作成する
    """
    mat = []

    for _ in range(nrow):
        r = []

        for _ in range(ncol):
            r.append(0)
        
        mat.append(r)
    
    return mat


def rotate_left():
    """
    行列を左に回転する
    """
    global mat

    dst = create_zero_matrix(len(mat), len(mat[0]))

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            dst[len(mat[j]) - 1 - j][i] = mat[i][j]
    
    mat = dst


def rotate_right():
    """
    行列を右に回転する
    """
    global mat

    dst = create_zero_matrix(len(mat), len(mat[0]))

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            dst[j][len(mat[i]) - 1 - i] = mat[i][j]
    
    mat = dst


def show():
    """
    行列を表示する
    """
    global mat

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            c = mat[i][j] # c ... component（成分）
            if c:
                print('★', end='')
            else:
                print('　', end='')
        print()
    

def main():
    # 出力
    show()

    # 無限ループ
    while True:
        # 入力
        try:
            cmd = input('command (L, R) > ')
        except (EOFError, KeyboardInterrupt):
            break
        
        # 回転処理
        if cmd == 'L':
            rotate_left()
        elif cmd == 'R':
            rotate_right()
        
        # 出力
        show()

    return 0


if __name__ == '__main__':
    sys.exit(main())
