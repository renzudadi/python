import random
from tkinter import *
from tkinter import messagebox
import tkinter as tk

def center_window(w, h):
    # 获取屏幕 宽、高
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def getsong():
    global songchosen
    songlist = open("songlist.txt", "r+")
    mysonglist = []
    for i in songlist:
        mysonglist.append(i)
    print("歌曲列表读取")
    songchosen = random.choice(mysonglist)
    songchosen = songchosen.replace("\n", "")
    return songchosen
def getaudience():
    global audience
    audiencelist = []
    audlist = open("audlist.txt", "r+")
    for i in audlist:
       audiencelist.append(i)
    print("观众列表读取")
    personchosen = random.choice(audiencelist)
    personchosen = personchosen.replace("\n", "")
    return personchosen
def update():
    global songchosen
    global personchosen
    songchosen = getsong()
    personchosen = getaudience()
    songlabel.config(text = songchosen)
    audlabel.config(text = personchosen)
    print("观众与歌曲更新完成")
def learnsong():
    global entry
    root2 = tk.Tk()
    label = tk.Label(root2, text='请输入歌名', font=('Arial', 12), width=15, height=2)
    label.pack()
    entry = tk.Entry(root2) # 创建一个输入框
    entry.pack()
    button = tk.Button(root2, text='确定', font=('Arial', 12), width=10, height=1, command=learn2)
    button.pack()
    root2.mainloop()
def learn2():
    song = entry.get()
    song = song+"\n"
    songlist = open("songlist.txt", "a")
    songlist.write(song)
    songlist.close()
    tk.messagebox.showinfo(title=None, message='歌曲添加成功')

def addaud():
    global entry
    root2 = tk.Tk()
    label = tk.Label(root2, text='请输入观众姓名', font=('Arial', 12), width=15, height=2)
    label.pack()
    entry = tk.Entry(root2) # 创建一个输入框
    entry.pack()
    button = tk.Button(root2, text='确定', font=('Arial', 12), width=10, height=1, command=addaud2)
    button.pack()
    root2.mainloop()
def addaud2():
    aud = entry.get()
    aud = aud+"\n"
    audlist = open("audlist.txt", "a")
    audlist.write(aud)
    audlist.close()
    tk.messagebox.showinfo(title=None, message='观众添加成功')

root = tk.Tk()
center_window(500, 480)
root.title("曼城周杰伦今日幸运粉丝连线程序")
menubar = Menu(root)
updatemenu = Menu(menubar, tearoff=0)
updatemenu.add_command(label="添加歌曲", command=learnsong)
updatemenu.add_command(label="添加观众", command=addaud)
updatemenu.add_separator()
updatemenu.add_command(label="退出", command=root.quit)
menubar.add_cascade(label="设置", menu=updatemenu)
root.config(menu=menubar)
w = tk.Label(root, text="被选中听歌的幸运粉丝是", font=("Arial", 12), width=30, height=2)
w.pack()
audlabel = tk.Label(root, text=getaudience(), font=("Arial", 12), bg = "pink",width=30, height=2)
audlabel.pack()
w = tk.Label(root, text="将收听到的歌曲是", font=("Arial", 12), width=30, height=2)
w.pack()
songlabel = tk.Label(root, text=getsong(), font=("Arial", 12), bg = "pink",width=30, height=2)
songlabel.pack()
w = tk.Label(root, text="让我们恭喜这位粉丝", font=("Arial", 12), width=30, height=2)
w.pack()
w = tk.Button(root, text="再来一次", font=("Arial", 12), width=30, height=2, command=update)
w.pack()
w = tk.Button(root, text="退出", font=("Arial", 12), width=30, height=2, command=root.quit)
w.pack()
root.mainloop()



