import sys


# 用于显示棋盘的常量
EMPTY_SPACE = "."  # 句点的数量比空格符更容易分辨
PLAYER_H = 'X'
PLAYER_L = 'O'

#注意，如果更新BOARD_WIDTH, 需要同时更新BOARD_TMEPLATE和COLUMN_LABELS
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABLES = ("1","2","3","4","5","6","7")
assert len(COLUMN_LABLES) == BOARD_WIDTH

# 用于显示棋盘的模板字符串：
BOARD_TEMPLATE = """
     1234567
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+ """

def main():
    """运行一局四子棋游戏"""
    print(
        """四子棋程序,作者是AI Sweigart
        两名玩家轮流将一颗棋子放入7列中的任意一列,试图在横、竖或对角方向上将自己的四颗棋子连成一条直线
        """
    )


    gameBoard = getNewBoard()
    # print(gameBoard)
    playerTurn = PLAYER_H

    while True: #  运行一个玩家的回合
        # 显示棋盘并获取玩家的移动方向
        displayBoard(gameBoard)
        playerMove = getPlayerMove(playerTurn, gameBoard)
        gameBoard[playerMove] = playerTurn

        # 检查是否取胜或者打平
        if isWinner(playerTurn, gameBoard):
            displayBoard(gameBoard) # 最后一次显示棋盘
            print("Player {} has won!".format(playerTurn))
            sys.exit()
        elif isFull(gameBoard):
            displayBoard(gameBoard) # 最后一次显示棋盘
            print("There is a tie!")
            sys.exit()

        # 轮到对手回合
        if playerTurn == PLAYER_H:
            playerTurn = PLAYER_L
        elif playerTurn == PLAYER_L:
            playerTurn = PLAYER_H


def getNewBoard():
    """返回代表四子棋棋盘的字典, 它的键是两个整数形成的元组
    (columnIndex, rowIndex), 值是字符串"X"、"0" 或者"."("."代表空格)
    """
    board = {}
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            board[(columnIndex, rowIndex)] = EMPTY_SPACE
    
    return board


def displayBoard(board):
    """在屏幕上展示棋盘和棋子"""

    # 准备传递给棋盘模板字符串的format()方法的列表
    # 列表中包含所有的棋子（以及空的格子），顺序是从左到右
    # 从上到下
    tileChars = []
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            tileChars.append(board[(columnIndex, rowIndex)])
    
    # 展示棋盘
    print(BOARD_TEMPLATE.format(*tileChars))


def getPlayerMove(playerTile, board):
    """让玩家选择要在棋盘的哪一列落子
    返回棋子所在的（列，行）的元组"""
    while True:  # 持续询问玩家， 直到输入有效的落子位置
        print(f"Player {playerTile}, enter 1 to {BOARD_WIDTH} or QUIT: ")
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        if response not in COLUMN_LABLES:
            print(f"Enter a number from 1 to {BOARD_WIDTH}")
            continue  # 再次询问玩家落子位置

        columnIndex = int(response) - 1  # 列索引是基于0的，-1 表示不存在

        # 如果这列满了， 再次要求玩家输入一个新的落子位置
        if board[columnIndex, 0]!= EMPTY_SPACE:
            print("That column is full, select another one.")
            continue  # 再次询问玩家落子位置

        # 自底向上寻找第一个空白格子：
        for rowIndex in range(BOARD_HEIGHT-1, -1,-1):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return(columnIndex, rowIndex)


def isFull(board):
    """如果board中没有空白格子,返回True,否则返回False"""
    for rowIndex in range(BOARD_WIDTH):
        for columnIndex in range(BOARD_HEIGHT):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return False  # 发现一个空白格子，返回False
            
    return True  # 格子全满了


def isWinner(playerTile, board):
    """如果棋盘上playerTile有四颗棋子连成一线, 返回True,否则返回False"""

    # 遍历整个棋盘，查找连成一线的四颗棋子
    for columnIndex in range(BOARD_WIDTH -3):
        for rowIndex in range(BOARD_HEIGHT):
            # 从左到右检查是否有四颗棋子连成一线
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex+1, rowIndex)]
            tile3 = board[(columnIndex+2, rowIndex)]
            tile4 = board[(columnIndex+3, rowIndex)]
            if tile1 ==  tile2 == tile3 == tile4 == playerTile:
                return True

    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT - 3):
            # 从上到下检查是否有连成一线的四颗棋子
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex, rowIndex+1)]
            tile3 = board[(columnIndex, rowIndex+2)]
            tile4 = board[(columnIndex, rowIndex+3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT - 3):
            # 从左上到右下的对角线上是否有连成一线的四颗棋子
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex+1, rowIndex+1)]
            tile3 = board[(columnIndex+2, rowIndex+2)]
            tile4 = board[(columnIndex+3, rowIndex+3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT- 3):
            # 从左下到右上的对角线上是否有连成一线的四颗棋子
            tile1 = board[(columnIndex+3, rowIndex)]
            tile2 = board[(columnIndex+2, rowIndex+1)]
            tile3 = board[(columnIndex+1, rowIndex+2)]
            tile4 = board[(columnIndex, rowIndex+3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True


# 如果这段代码被运行（而不是被导入），运行游戏：
if __name__=="__main__":
    main()