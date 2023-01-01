# 一个OOP井字游戏
import copy

All_SPACES = list('123456789')  # 井字棋棋盘字典的键
X, O, BLANK = 'X', 'O', '-' # 字符串值常量


def main():
    """运行一局井字棋游戏"""
    print('Welcome to tic-tac-toe!')
    """选择在普通井字棋棋盘 、 简化井字棋棋盘中二选一的可能性"""
    # if input('Use mini board? Y/N: ').lower().startswith('y'):
    #     gameBoard = MiniBoard()  # 创建一个井字棋棋盘对象
    # else:
    #     gameBoard = TTTBoard()  # 创建一个井字棋棋盘对象
    """创建一个棋盘能自动的预测下一步获胜的棋盘"""
    gameBoard = HintBoard()   # 创建一个能自动预测下一步获胜的棋盘
    currentPlayer, nextPlayer = X, O # X 先行， O 后行

    while True:
        print(gameBoard.getBoardStr())  # 屏幕上显示棋盘

        # 询问玩家，直到玩家输入数字1-9
        move = None

        while not gameBoard.isValidSpace(move):
            print(f'What is {currentPlayer} player\'s move? (1-9)')
            move = input()
        gameBoard.updateBoard(move, currentPlayer) # 执行移动

        # 检查游戏是否结束：
        if gameBoard.isWinner(currentPlayer):  # 首先检查一方是否获胜
            print(gameBoard.getBoardStr())
            print(currentPlayer + ' player has won the game!')
            break
        elif gameBoard.isBoardFull():  # 接着检查是否平局
            print(gameBoard.getBoardStr())
            print('The game is a tie!')
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer  # 交换玩家
    print('Thanks for playing!')


class TTTBoard:
    def __init__(self, usePrettyBoard = False, useLogging = False):
        """创建新的空白井字棋棋盘"""
        self._spaces = {}  # 使用Python字典表示棋盘
        for space in All_SPACES:
            self._spaces[space] = BLANK  # 所有格子起初都是空格子
        
    def getBoardStr(self):
        """返回棋盘的字符串表示"""
        return f'''
        {self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']}  1 | 2 | 3
        
        {self._spaces['4']}|{self._spaces['5']}|{self._spaces['6']}  4 | 5 | 6
        
        {self._spaces['7']}|{self._spaces['8']}|{self._spaces['9']}  7 | 8 | 9'''

    def isValidSpace(self, space):
        """当棋盘中的格子数有效， 且该格子为空白时, 返回True"""
        return space in All_SPACES and self._spaces[space] == BLANK

    def isWinner(self, player):
        """当玩家在井字棋棋盘上是赢家时返回True"""
        s, p = self._spaces, player  # 使用缩写作为 “语法糖”
        # 检查3行，3列，2条对角线上的3个标记
        return ((s['1']==s['2']==s['3']==p) or  # 顶部行
                (s['4']==s['5']==s['6']==p) or  # 中间行
                (s['7']==s['8']==s['9']==p) or  # 底部行
                (s['1']==s['4']==s['7']==p) or  # 左边列
                (s['2']==s['5']==s['8']==p) or  # 中间列
                (s['3']==s['6']==s['9']==p) or  # 右边列
                (s['1']==s['5']==s['9']==p) or  # 对角线
                (s['3']==s['5']==s['7']==p))    # 对角线

    def isBoardFull(self):
        """当棋盘上的每个格子都被使用时返回True"""
        for space in All_SPACES:
            if self._spaces[space] == BLANK:
                return False  # 如果有任意一个格子是空白的，返回False
        return True  # 如果没有一个格子是空白的，返回True

    def updateBoard(self, space, player):
        """将棋盘上的格子设置为标记符"""
        self._spaces[space] = player


class MiniBoard(TTTBoard):
    def getBoardStr(self):
        """返回一个用文字表示的小键盘"""
        # 将空格设为“.”
        for space in All_SPACES:
            if self._spaces == BLANK:
                self._spaces[space] = '.'

        boardStr = f'''
        {self._spaces['1']}{self._spaces['2']}{self._spaces['3']}   123
        {self._spaces['4']}{self._spaces['5']}{self._spaces['6']}   456
        {self._spaces['7']}{self._spaces['8']}{self._spaces['9']}   789'''

        # 将“.”需改回空格子
        for space in All_SPACES:
            if self._spaces[space] == ".":
                self._spaces[space] = BLANK
        
        return boardStr

    
class HintBoard(TTTBoard):
    def getBoardStr(self):
        """返回一个带提示的, 用文字表示的棋盘"""
        boardStr =  super().getBoardStr()  # 调用TTTBoard中的getBoardStr()方法

        xCanWin = False
        oCanWin = False
        originalSpaces = self._spaces  # 将spaces备份
        for space in All_SPACES:

            """
            自动设置了往下走一步，遍历了所有的棋盘，找出可能再下一步取胜的可能
            """
            #  模拟玩家X移动到了该空格子
            self._spaces = copy.deepcopy(originalSpaces)
            if self._spaces[space] == BLANK:
                self._spaces[space] = X
            if self.isWinner(X):  # 调用了父类TTTBoard中的isWinner()方法
                xCanWin = True
                print('Xplayer space location is: ', space)
            #  模拟玩家O移动到了该空格子
            self._spaces = copy.deepcopy(originalSpaces)
            if self._spaces[space] == BLANK:
                self._spaces[space] = O
            if self.isWinner(O):  # 调用了父类TTTBoard中的isWinner()方法
                oCanWin = True
                print('Oplayer space location is: ', space)
        
        if xCanWin:
            boardStr += '\nX can win in one more move.'
        if oCanWin:
            boardStr += '\nO can win in one more move.'
        self._spaces = originalSpaces  # 返回现在的棋盘
        return boardStr
           


if __name__=='__main__':
    main()  # 当模块被直接运行而非被引入时，调用main()