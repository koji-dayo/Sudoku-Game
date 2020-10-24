import tkinter as tk
import numpy as np

class Game(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        self.width = 540
        self.height = 540
        self.chip = 0
        #ビギナー問題参照
        self.map_data = [
            [8,12,9,0,7,0],
            [10,0,0,12,8,0],
            [11,0,10,0,12,0],
            [0,9,7,0,10,0],
            [0,10,0,0,11,0],
            [0,0,0,0,0,8],
        ]
        master.geometry(str(self.width) + "x" + str(self.height))
        master.title("数独")
        self.createWidgets()

    def createWidgets(self):
        self.cvs_bg = tk.Canvas(width=360, height=360, bg="black")
        self.cvs_bg.place(x=10, y=10)
        self.cvs_bg.bind("<Button-1>", self.set_map)
        self.cvs_bg.bind("<B1-Motion>", self.set_map)

        self.cvs_chip = tk.Canvas(width=60, height=440, bg="black")
        self.cvs_chip.place(x=420, y=10)
        self.cvs_chip = tk.Canvas(width=60, height=440, bg="black")
        self.cvs_chip.place(x=420, y=10)
        self.cvs_chip.bind("<Button-1>", self.select_chip)
        self.btn = tk.Button(text="回答する", font=("Times New Roman", 20), fg="blue", command=self.put_data)
        self.btn.place(x=180, y=400)
        self.img = [
        tk.PhotoImage(file="image/black.png"),
        tk.PhotoImage(file="image/one.png"),
        tk.PhotoImage(file="image/two.png"),
        tk.PhotoImage(file="image/three.png"),
        tk.PhotoImage(file="image/four.png"),
        tk.PhotoImage(file="image/five.png"),
        tk.PhotoImage(file="image/six.png"),
        tk.PhotoImage(file="image/onered.png"),#初期値の数字1
        tk.PhotoImage(file="image/twored.png"),#初期値の数字2
        tk.PhotoImage(file="image/threered.png"),#初期値の数字3
        tk.PhotoImage(file="image/fourred.png"),#初期値の数字4
        tk.PhotoImage(file="image/fivered.png"),#初期値の数字5
        tk.PhotoImage(file="image/sixred.png")#初期値の数字6
        ]
        self.draw_map()
        self.draw_chip()

    #mapに画像を埋め込む(初期値は)
    def draw_map(self):
        self.cvs_bg.delete("BG")
        for y in range(6):
            for x in range(6):
                self.cvs_bg.create_image(60*x+30, 60*y+30, image=self.img[self.map_data[y][x]], tag="BG")
    #マップ画像更新
    def set_map(self,e):
        x = int(e.x/60)
        y = int(e.y/60)
        if 0 <= x and x <= 5 and 0 <= y and y <= 5:
            if self.map_data[y][x] <=6:#もし初期値の数字(与えられる問題の数字)じゃない場合、数字を書き込めるようにする。
                self.map_data[y][x] = self.chip
                self.draw_map() 

    #数字出力(右側)
    def select_chip(self,e):
        #global chip
        y = int(e.y/60)
        if 0 <= y and y < 7:
            self.chip = y
            self.draw_chip()
    
    #数字出力(右側)
    def draw_chip(self):
        self.cvs_chip.delete("CHIP")
        for i in range(7):
            self.cvs_chip.create_image(30, 30+i*60, image=self.img[i], tag="CHIP")
        self.cvs_chip.create_rectangle(4, 4+60*self.chip, 57, 57+60*self.chip, outline="red", width=3, tag="CHIP")

    #データ出力
    def put_data(self):
        #正解を確認する
        for y in range(0,6):
            for x in range(0,6):
                if self.map_data[y][x] == 7:
                    self.map_data[y][x] = 1
                if self.map_data[y][x] == 8:
                    self.map_data[y][x] = 2
                if self.map_data[y][x] == 9:
                    self.map_data[y][x] = 3
                if self.map_data[y][x] == 10:
                    self.map_data[y][x] = 4
                if self.map_data[y][x] == 11:
                    self.map_data[y][x] = 5
                if self.map_data[y][x] == 12:
                    self.map_data[y][x] = 6
        count = 0
        for y in range(0,6):
            if sum(self.map_data[y]) == 21:
                if len(self.map_data[y]) == len(set(self.map_data[y])):
                    count += 1
        map_data_T = np.array(self.map_data).T.tolist()
        for y in range(0,6):
            if sum(map_data_T[y]) == 21:
                if len(map_data_T[y]) == len(set(map_data_T[y])):
                    count += 1

        if count == 12:
            self.draw_txt("ゲームクリア",170,270,30,"pink")
            
        else:
            self.draw_txt("不正解！！",170,270,30,"blue")
           
    def draw_txt(self,txt, x, y, siz, col): # 文字をウィンドウに表示する
        fnt = ("Times New Roman", siz, "bold")
        self.cvs_bg.create_text(x+2, y+2, text=txt, fill="black", font=fnt, tag="SCREEN")
        self.cvs_bg.create_text(x, y, text=txt, fill=col, font=fnt, tag="SCREEN")
def main():
    root = tk.Tk()
    root.resizable(width=False, height=False) 
    game = Game(master = root)
    game.mainloop()

if __name__ == '__main__':
    main()
