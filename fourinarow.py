import sys

EMPTY_SPACE = "."
PLAYER_H = 'X'
PLAYER_L = 'O'


BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABLES = ("1","2","3","4","5","6","7")
assert len(COLUMN_LABLES) == BOARD_WIDTH


BOARD_TEMPLATE = """
 1234567
+-------+
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
+-------+"""

def main():
    """运行一局四子棋游戏"""
    print(
        """四子棋程序,作者是AI Sweigart
        两名玩家轮流将一颗棋子放入7列中的任意一列,试图在横、竖或对角方向上将自己的四颗棋子连成一条直线
        """
    )


    gameBoard = getNewBoard()
    playerTurn = PLAYER_H

    while True: #  运行一个玩家的回合
        # 显示棋盘并获取玩家的移动方向
        displayBoard(gameBoard)
        playerMove = getPlayMove(playerTurn, gameBoard)
        gameBoard[playerMover] = playerTurn

        # 检查是否取胜或者打平
        if isWinner(playTurn, gameBoard):
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
             