import os
import sys

class DFS():

    # データを初期化
    def __init__(self):

        # 小枠の大きさ
        self.n = 3
        self.m=2

        # 大枠と数値の終端を定義

        #self.N = self.n * self.n
        self.N = self.n*self.m
        # 問題の全ての配列を0で初期化する
        self.question = [[0 for i in range((self.N))] for j in range((self.N))]

    # 横行に答えがあっているか調べる
    def checkQuestionRow(self,Row):

        # 1～Nの数字がいくつ含まれるかを格納する配列
        num = [0 for m in range((self.N + 1))]

        # 横0行目～横(N-1)行目までを走査する
        for x in range(0,self.N):

            # 1～Nがいくつ含まれるか調べる
            for m in range(1,self.N+1):

                    #(x,Row)のマス目の値がmのとき
                    if m == self.question[x][Row]:

                        # 数字がmの個数に+1する
                        num[m] = num[m] + 1

        # 列Row内で、数字が2つ以上使われて場合はFalseを返す
        for m in range(1,self.N+1):
            if num[m] > 1:
                return False

        return True

    # 縦:列Colにおいて、1～Nの数字が1つずつ出現しているか調べる
    # 基本、checkQuestionRowと同じ動作
    def checkQuestionCol(self,Col):

        # 1～Nの数字がいくつ含まれるかを格納する配列
        num = [0 for m in range((self.N + 1))]

        # 縦0列目～横(N-1)列目までを走査する
        for y in range(0,self.N):
            for m in range(1,self.N+1):
                    if m == self.question[Col][y]:
                        num[m] = num[m] + 1

        # 列内で、数字が2つ以上使われて場合はFalseを返す
        for m in range(1,self.N+1):
            if num[m] > 1:
                return False

        return True

    # 2*2，3*3のブロックごとに、1～Nの数字が1つずつ出現しているか調べる
    def checkQuestionBlock(self,rowBlock,colBlock):

        # ブロックの開始地点(colBlock* n ,rowBlock* n)を定義
        startCol = colBlock * self.n
        startRow = rowBlock * self.m

        # ブロックの終了地点(colBlock* {n+1} ,rowBlock* {n+1})を定義
        endCol =  (colBlock + 1) * (self.n)
        endRow =  (rowBlock + 1) * (self.m)

        # 1～Nの数字がいくつ含まれるかを格納する配列
        num = [0 for m in range((self.N + 1))]

        # ブロック毎に走査を行う
        for y in range(startCol,endCol):
            for x in range(startRow,endRow):
                for m in range(1,self.N+1):
                    if m == self.question[y][x]:
                        num[m] = num[m] + 1

        # ブロック内で、数字が2つ以上使われて場合はFalseを返す
        for m in range(1,self.N+1):
            if num[m] > 1:
                return False

        return True

    # 現在の(x,y)の解が合っているかどうか調べる
    def checkQuestion(self,x,y):

        # まず全ての行RowにNまでの数字が含まれているか調べる
        if self.checkQuestionRow(x) == False:
            return False

        # 次に全ての列Colに１～Nまでの数字が含まれているか調べる
        if self.checkQuestionCol(y) == False:
            return False

        # 最後にブロック毎に１～Nまでの数字が含まれているか調べる
        colBlock = x // self.n
        rowBlock = y // self.m
        if self.checkQuestionBlock(colBlock,rowBlock) == False:
            return False

        return True

    # 深さ優先探索より、数独の解を探索する
    def solve(self,question,x=0,y=0):

        # 最終列の次の列に差し掛かったら、再帰を終了する
        if x == 0 and y == self.N:
            return True

        # マス目に既に数字が置かれているとき
        if self.question[y][x] != 0:

            if x == self.N-1:
                if self.solve(self.question,0,y+1):
                    return True
            else:
                if self.solve(self.question,x+1,y):
                    return True

        # マス目に数字が置かれていないとき
        else:

            for m in range(1,self.N+1):
                self.question[y][x] = m
                # デバッグ用
                # print("(x,y,i) = (" + str(x) + "," + str(y) + "," + str(self.question[y][x]) + ")")

                if self.checkQuestion(x,y) == True:
                    self.question[y][x] = m

                    if x == self.N-1:
                        if self.solve(self.question,0,y+1):
                            return True
                    else:
                        if self.solve(self.question,x+1,y):
                            return True

            self.question[y][x] = 0
            # デバッグ用
            # print("(x,y,i) = (" + str(x) + "," + str(y) + "," + str(self.question[y][x]) + ")")
            return False
