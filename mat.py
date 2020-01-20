"""
入力に応じて行列を回転して表示するスクリプトです
"""
import sys

"""
11 12 13 14
21 22 23 24
31 32 33 34
41 42 43 44

左回転

11 -> 41
12 -> 31
13 -> 21
14 -> 11

右回転

11 -> 14
12 -> 24
13 -> 34
14 -> 44

"""


# 操作対象の行列
m44 = [
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 0],
]


def create_zero_m44():
    """
    4x4の零行列を作成する
    """
    return [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]


def rotate_left():
    """
    行列を左に回転する
    """
    global m44

    dst44 = create_zero_m44()

    for i in range(len(m44)):
        for j in range(len(m44[i])):
            dst44[3 - j][i] = m44[i][j]
    
    m44 = dst44


def rotate_right():
    """
    行列を右に回転する
    """
    global m44

    dst44 = create_zero_m44()

    for i in range(len(m44)):
        for j in range(len(m44[i])):
            dst44[j][3 - i] = m44[i][j]
    
    m44 = dst44


def show():
    """
    行列を表示する
    """
    global m44

    for i in range(len(m44)):
        for j in range(len(m44[i])):
            c = m44[i][j] # c ... component（成分）
            if c:
                print('■', end='')
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
