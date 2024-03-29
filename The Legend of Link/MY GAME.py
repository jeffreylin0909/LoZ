#import 所需模組
import time
import tkinter as tk
import threading as th
import os
from random import randint, choice
###123
#創建基本GUI
root=tk.Tk()
###
#引進遊戲所需圖像
linkwf = tk.PhotoImage(file = "gameobject\\link.gif")
linkr=w=tk.PhotoImage(file='gameobject\\linkr.gif')
linkl=w=tk.PhotoImage(file='gameobject\\linkl.gif')
linkwl=w=tk.PhotoImage(file='gameobject\\linkwl.gif')
linkwr=w=tk.PhotoImage(file='gameobject\\linkwr.gif')
linkwb=w=tk.PhotoImage(file='gameobject\\linkwb.gif')
linkf=w=tk.PhotoImage(file='gameobject\\linkf.gif')
linkb=w=tk.PhotoImage(file='gameobject\\linkb.gif')
mon=tk.PhotoImage(file='gameobject\\monster.gif')
mon2=tk.PhotoImage(file='gameobject\\monster2.gif')
hart=tk.PhotoImage(file='gameobject\\hart.gif')
hart0=tk.PhotoImage(file='gameobject\\hart_black.gif')
none=tk.PhotoImage(file='gameobject\\hart0.gif')
w=tk.PhotoImage(file='gameobject\\wall.gif')
w1=tk.PhotoImage(file='gameobject\\wall1.gif')
gameover=tk.PhotoImage(file='gameobject\\gameover.gif')
Sign=tk.PhotoImage(file='gameobject\\sign.gif')
logo=tk.PhotoImage(file='gameobject\\logo.gif')
PST_image=tk.PhotoImage(file='gameobject\\press to start.gif')
Paused_image=tk.PhotoImage(file='gameobject\\paused.gif')
endgame_image=tk.PhotoImage(file='gameobject\\sword.gif')
get_sword_image=tk.PhotoImage(file='gameobject\\get_sword.gif')
###
#宣告list
wall_list=[]
monster_list=[]
hart_container_list=[]
###
#各物件,各關卡座標資料
wall_static_list=[
[20,30],[20,80],[20,130],[20,180],[20,230],
[20,430],[20,480],[20,530],[20,580],[20,630],
[1255,30],[1255,80],[1255,130],[1255,180],
[1255,230],[1255,430],[1255,480],[1255,530],
[1255,580],[1255,630],
[20,25],[70,25],[120,25],[170,25],
[220,25],[270,25],[320,25],[370,25],
[420,25],[470,25],[770,25],[820,25],
[870,25],[920,25],[970,25],[1020,25],
[1070,25],[1120,25],[1170,25],[1220,25],[1270,25],
[20,630],[70,630],[120,630],[170,630],
[220,630],[270,630],[320,630],[370,630],
[420,630],[470,630],[770,630],[820,630],
[870,630],[920,630],[970,630],[1020,630],
[1070,630],[1120,630],[1170,630],[1220,630],[1270,630]
]
hart_list=[[255,30,-1],[230,30,-1],[205,30,-1],[180,30,-1],[155,30,-1],[130,30,-1],[105,30,-1],[80,30,1],[55,30,1],[30,30,1]]
wall_move_list_LV1=[[620,350],[670,350],[570,350],[620,400],[520,350],[720,350],[-20,-20],[-20,-20],[-20,-20],[-20,-20],[-20,-20],[-20,-20],[-20,-20],[-20,-20]]
wall_move_list_LV2=[[130,350],[1140,350],[180,400],[1090,400],[180,450],[1090,450],[180,350],[1090,350],[-20,-20],[-20,-20],[-20,-20],[-20,-20],[-20,-20],[-20,-20]]
wall_move_list_LV3=[[620,350],[670,350],[570,350],[620,450],[520,350],[720,350],[520,450],[720,450],[-20,-20],[-20,-20],[-20,-20],[-20,-20],[-20,-20],[-20,-20]]
wall_move_list_LV4=[[520,300],[570,300],[670,400],[720,400],[620,350],[470,250],[770,450],[-20,-20],[-20,-20],[-20,-20],[-20,-20],[-20,-20],[-20,-20],[-20,-20]]
wall_move_list_LV5=[[520,300],[570,300],[620,300],[670,300],[720,300],[520,350],[570,400],[720,350],[670,400],[-20,-20],[-20,-20],[-20,-20],[-20,-20],[-20,-20]]
wall_move_list_LV6=[[-50,-50],[-50,-50],[-50,-50],[-50,-50],[-50,-50],[-50,-50],[-50,-50],[-20,-20],[-20,-20],[-20,-20],[-20,-20],[-20,-20],[-20,-20],[-20,-20]]
wall_move_list_LV7=[[520,300],[570,300],[620,300],[670,300],[720,300],[520,500],[570,500],[620,500],[670,500],[720,500],[670,350],[620,400],[570,450],[-20,-20]]
wall_move_list_LV8=[[570,300],[620,300],[670,300],[720,300],[570,350],[570,400],[570,450],[570,500],[620,500],[670,500],[720,500],[620,400],[670,400],[720,400]]
wall_move_list_LV9=[[570,300],[570,350],[570,400],[570,450],[570,500],[620,500],[670,500],[720,500],[-20,-20],[-20,-20],[-20,-20],[-20,-20],[-20,-20],[-20,-20]]
wall_move_list_LV10=[[570,300],[570,350],[570,400],[570,450],[570,500],[620,500],[670,500],[620,300],[670,300],[720,350],[720,400],[720,450],[-20,-20],[-20,-20]]
wall_move_list_LV11=[[620,250],[640,300],[600,300],[660,350],[580,350],[680,400],[560,400],[700,450],[540,450],[720,500],[520,500],[670,400],[620,400],[570,400]]
wall_move_list_LV12=[[-50,-50],[-50,-50],[-50,-50],[-50,-50],[-50,-50],[-50,-50],[-50,-50],[-20,-20],[-20,-20],[-20,-20],[-20,-20],[-20,-20],[-20,-20],[-20,-20]]
wall_move_list_LV13=[[130,350],[1140,350],[180,400],[1090,400],[180,450],[1090,450],[180,350],[1090,350],[-20,-20],[-20,-20],[-20,-20],[-20,-20],[-20,-20],[-20,-20]]
wall_move_list=[wall_move_list_LV1,wall_move_list_LV2,wall_move_list_LV3,wall_move_list_LV4,
wall_move_list_LV5,wall_move_list_LV6,wall_move_list_LV7,wall_move_list_LV8,
wall_move_list_LV9,wall_move_list_LV10,wall_move_list_LV11,wall_move_list_LV12,wall_move_list_LV13]
monster_list_LV1=[[510,400,5,1,1],[730,400,-5,1,1]]
monster_list_LV2=[[130,400,5,2,1],[1140,400,5,2,1]]
monster_list_LV3=[[670,400,5,2,1],[570,400,5,2,1]]
monster_list_LV4=[[570,350,-5,1,1],[670,350,5,1,1]]
monster_list_LV5=[[570,350,-5,2,1],[670,350,-5,2,1]]
monster_list_LV6=[[-50,-50,-5,3,1],[-50,-50,5,3,1]]
monster_list_LV7=[[520,350,5,1,2],[720,450,-5,1,2]]
monster_list_LV8=[[620,350,5,1,2],[620,450,5,1,2]]
monster_list_LV9=[[620,450,5,1,2],[620,450,-5,2,2]]
monster_list_LV10=[[720,500,5,1,2],[720,300,5,1,2]]
monster_list_LV11=[[670,500,-5,1,2],[570,500,5,1,2]]
monster_list_LV12=[[-50,-50,-5,3,1],[-50,-50,5,3,1]]
monster_list_LV13=[[-50,-50,-5,3,1],[-50,-50,5,3,1]]
monster_move_list=[monster_list_LV1,monster_list_LV2,monster_list_LV3,monster_list_LV4,
monster_list_LV5,monster_list_LV6,monster_list_LV7,monster_list_LV8,
monster_list_LV9,monster_list_LV10,monster_list_LV11,monster_list_LV12,monster_list_LV13]
###
#GUI基本設定
root.title('The Legend of Zelda')
root.geometry('1280x650')
root.iconphoto(True,logo)
#是否進行遊戲的變數
started=0
#是否pause的變數
notpaused=1
#目前的關卡數
level=1
###
#class主角
class main_character():
    def __init__(self,x,y,imag):
        self.is_alive=True#是否活著
        self.image= canvas.create_image(x,y,anchor='center',image=imag)
        self.dire='f'#目前方向
        self.attack='c'#是否在攻擊畫面&攻擊方向

    def delete(self):
        self.is_alive=False
        canvas.itemconfig(self.image,image=none)

    def walk(self,code):
        global link
        if self.is_alive==True:
            if chr(code)=='A' or chr(code)=='a':
                canvas.itemconfig(self.image, image = linkwl)
                self.dire='l'
                canvas.move(self.image,-5,0)

            if chr(code)=='D' or chr(code)=='d':
                canvas.itemconfig(self.image, image = linkwr)
                self.dire='r'
                canvas.move(self.image,5,0)

            if chr(code)=='W' or chr(code)=='w':
                canvas.itemconfig(self.image, image = linkwb)
                self.dire='b'
                canvas.move(self.image,0,-5)

            if chr(code)=='S' or chr(code)=='s':
                canvas.itemconfig(self.image, image = linkwf)
                self.dire='f'
                canvas.move(self.image,0,5)

            if code==32:
                if self.dire=='f':
                    canvas.itemconfig(self.image, image = linkf)
                    self.attack='f'
                    th.Timer(0.3,back_to_stand).start()
                if self.dire=='l':
                    canvas.itemconfig(self.image, image = linkl)
                    self.attack='l'
                    th.Timer(0.3,back_to_stand).start()
                if self.dire=='r':
                    canvas.itemconfig(self.image, image = linkr)
                    self.attack='r'
                    th.Timer(0.3,back_to_stand).start()
                if self.dire=='b':
                    canvas.itemconfig(self.image, image = linkb)
                    self.attack='b'
                    th.Timer(0.3,back_to_stand).start()
            for i in wall_list:
                i.block(code)

    def is_hurt(self,code,move):
        if chr(code)=='A' or chr(code)=='a':
            canvas.move(self.image,move,0)
        if chr(code)=='D' or chr(code)=='d':
            canvas.move(self.image,-move,0)
        if chr(code)=='W' or chr(code)=='w':
            canvas.move(self.image,0,move)
        if chr(code)=='S' or chr(code)=='s':
            canvas.move(self.image,0,-move)
    
    def move_to(self,x,y,dire):
        self.dire=dire
        canvas.move(self.image,x-canvas.coords(self.image)[0],y-canvas.coords(self.image)[1])
###
#class小怪
class monster():
    def __init__(self,x,y,step,dire,lives):
        self.image=canvas.create_image(x,y,anchor='center',image=mon)
        self.step = step
        self.dire=dire
        self.x=x
        self.y=y
        self.lives=lives
        monster_list.append(self)

    def delete(self):
        th.Thread(target=self.die_config).start()
        self.die_count=0

    def move(self):
        if self.lives:
            if self.lives==1:
                canvas.itemconfig(self.image,image=mon)
            elif self.lives==2:
                canvas.itemconfig(self.image,image=mon2)
            if self.dire==1:
                if canvas.coords(self.image):
                    canvas.move(self.image,self.step,0)
                    if canvas.coords(self.image)[0]==self.x or canvas.coords(self.image)[0]==self.x + self.step * 12:
                        self.step = -self.step
            if self.dire==2:
                if canvas.coords(self.image):
                    canvas.move(self.image,0,self.step)
                    if canvas.coords(self.image)[1]==self.y or canvas.coords(self.image)[1]== self.y + self.step * 12:
                        self.step = -self.step

    def can_attack_or_not(self):
        if self.lives and link.is_alive==True:
            if abs(canvas.coords(link.image)[0] - canvas.coords(self.image)[0]) < 30 and abs(canvas.coords(link.image)[1] - canvas.coords(self.image)[1])<30:
                for i in hart_container_list:
                    if i.e==1:
                        canvas.itemconfig(i.image,image=hart0)
                        i.e=0
                        if link.dire=='f':
                            link.is_hurt(ord('s'),40)
                        if link.dire=='r':
                            link.is_hurt(ord('d'),40)
                        if link.dire=='l':
                            link.is_hurt(ord('a'),40)
                        if link.dire=='b':
                            link.is_hurt(ord('w'),40)
                        break

                    if hart_container_list[-2].e==0:
                        link.delete()
                        canvas.itemconfig(GG,image=gameover)
                        th.Timer(3,end).start()
                        hart_container_list[-1].e=0
                        canvas.itemconfig(hart_container_list[-1].image,image=hart0)
                        break

                    
    def is_dead_or_not(self,code):
        if self.lives and link.is_alive==True:
            if abs(canvas.coords(link.image)[0] - canvas.coords(self.image)[0]) < 50 and abs(canvas.coords(link.image)[1] - canvas.coords(self.image)[1])<50:
                if code==32:
                    if abs(canvas.coords(self.image)[0]-canvas.coords(link.image)[0])>abs(canvas.coords(self.image)[1]-canvas.coords(link.image)[1]):
                        if canvas.coords(self.image)[0]>canvas.coords(link.image)[0]:
                            canvas.itemconfig(link.image, image = linkr)
                            link.attack='r'
                            th.Timer(0.3,back_to_stand).start()
                        else:
                            canvas.itemconfig(link.image, image = linkl)
                            link.attack='l'
                            th.Timer(0.3,back_to_stand).start()
                    else:
                        if canvas.coords(self.image)[1]>canvas.coords(link.image)[1]:
                            canvas.itemconfig(link.image, image = linkf)
                            link.attack='f'
                            th.Timer(0.3,back_to_stand).start()
                        else:
                            canvas.itemconfig(link.image, image = linkb)
                            link.attack='b'
                            th.Timer(0.3,back_to_stand).start()
                    self.lives-=1
                    if self.lives==0:
                        self.delete()
                        kills.set(kills.get() + 1)

    def die_config(self):
        for i in range(10):
            time.sleep(0.07)
            if (i%2==0):
                canvas.itemconfig(self.image,image=mon)
            if (i%2==1):
                canvas.itemconfig(self.image,image=none)

    def move_to(self,x,y,step,dire,lives):
        self.x=x
        self.y=y
        self.dire=dire
        self.step=step
        self.lives=lives
        canvas.move(self.image,x-canvas.coords(self.image)[0],y-canvas.coords(self.image)[1])
###
#class牆
class wall():
    def __init__(self,x,y,img):
        self.image=canvas.create_image(x,y,anchor='center',image=img)
        wall_list.append(self)
        
    def block(self,code):
        if canvas.coords(link.image):
            if abs(canvas.coords(link.image)[0] - canvas.coords(self.image)[0]) < 45 and abs(canvas.coords(link.image)[1] - canvas.coords(self.image)[1])<45:
                link.is_hurt(code,5)
    def move_to(self,x,y):
        canvas.move(self.image,x-canvas.coords(self.image)[0],y-canvas.coords(self.image)[1])
###
#class血量
class hart_container():
    def __init__(self,x,y,e):
        hart_container_list.append(self)
        self.e=e
        if e==-1:
            self.image=canvas.create_image(x,y,anchor='center',image=none)
        else:
            self.image=canvas.create_image(x,y,anchor='center',image=hart)
###
#定義鍵盤callback程序       
def callback(event):
    global started
    global notpaused
    if started and notpaused:
            link.walk(event.keycode)
            for i in monster_list:
                i.is_dead_or_not(event.keycode)
            if abs(canvas.coords(link.image)[0] - canvas.coords(sign)[0]) < 50 and abs(canvas.coords(link.image)[1] - canvas.coords(sign)[1])<50:
                if event.keycode==32:
                    if kills.get()>=5:
                        for i in hart_container_list:
                            if i.e==1 or i.e==0:
                                hart_container_list[hart_container_list.index(i)-1].e=1
                                canvas.itemconfig(hart_container_list[hart_container_list.index(i)-1].image,image=hart)
                                for i in hart_container_list:
                                    if i.e==0:
                                        i.e=1
                                        canvas.itemconfig(i.image,image=hart)
                                break
                        kills.set(kills.get() -5)
            if abs(canvas.coords(link.image)[0] - canvas.coords(endgame)[0]) < 100 and abs(canvas.coords(link.image)[1] - canvas.coords(endgame)[1])<100:
                if event.keycode==32:
                    gets()
    elif started==0 and event.keycode==32:
        started=1
        start()

###
#定義計時器callback程序
def timer_callback():
    global started
    global notpaused
    if not started:
        return
    if notpaused:
        for i in monster_list:
            i.move()
            i.can_attack_or_not()
        if link.is_alive:
            if canvas.coords(link.image)[1]>700:
                link.move_to(620,20,'f')
                th.Thread(target=next_level).start()

            elif canvas.coords(link.image)[0]<-20:
                link.move_to(1275,350,'l')
                th.Thread(target=next_level).start()

            elif canvas.coords(link.image)[0]>1275:
                link.move_to(-20,350,'r')
                th.Thread(target=next_level).start()

            elif canvas.coords(link.image)[1]<-20:
                link.move_to(620,670,'b')
                th.Thread(target=next_level).start()

    th.Timer(0.05, timer_callback).start()
###
#定義讓主角在攻擊後回到站立姿勢的程序
def back_to_stand():
    global started
    global notpaused
    if not started:
        return
    if notpaused:
        if link.is_alive==True:
            if link.attack=='l':
                canvas.itemconfig(link.image, image = linkwl)
                link.attack='c'
            if link.attack=='r':
                canvas.itemconfig(link.image, image = linkwr)
                link.attack='c'
            if link.attack=='f':
                canvas.itemconfig(link.image, image = linkwf)
                link.attack='c'
            if link.attack=='b':
                canvas.itemconfig(link.image, image = linkwb)
                link.attack='c'
###
#定義主角出場的程序
def showup():
    global started
    global notpaused
    if not started:
        return
    if notpaused:
        if link.is_alive:
            if link.dire=='f':
                while canvas.coords(link.image)[1]<=30:
                    canvas.move(link.image,0,5)
                    time.sleep(0.05)
            if link.dire=='b':
                while canvas.coords(link.image)[1]>=620:
                    canvas.move(link.image,0,-5)
                    time.sleep(0.05)
            if link.dire=='r':
                while canvas.coords(link.image)[0]<=20:
                    canvas.move(link.image,5,0)
                    time.sleep(0.05)
            if link.dire=='l':
                while canvas.coords(link.image)[0]>=1235:
                    canvas.move(link.image,-5,0)
                    time.sleep(0.05)
###
#定義讓主角前往下一關的程序
def next_level():
    global level
    global started
    global notpaused
    if not started:
        return
    if notpaused:
        if level==len(monster_move_list):
            level=1
        else:
            level+=1
        if level%6==0:
            canvas.move(sign,620-canvas.coords(sign)[0],400-canvas.coords(sign)[1])
        else:
            canvas.move(sign,-500-canvas.coords(sign)[0],-500-canvas.coords(sign)[1])
        if level==len(monster_move_list):
            canvas.move(endgame,620-canvas.coords(endgame)[0],400-canvas.coords(endgame)[1])
        else:
            canvas.move(endgame,-500-canvas.coords(endgame)[0],-500-canvas.coords(endgame)[1])
        link.show=0
        for i in monster_list:
            i.move_to(monster_move_list[level-1][monster_list.index(i)][0],monster_move_list[level-1][monster_list.index(i)][1],monster_move_list[level-1][monster_list.index(i)][2],monster_move_list[level-1][monster_list.index(i)][3],monster_move_list[level-1][monster_list.index(i)][4])
        for i in wall_list:
            i.move_to(wall_move_list[level-1][wall_list.index(i)][0],wall_move_list[level-1][wall_list.index(i)][1])
            if wall_list.index(i)==len(wall_move_list_LV1)-1:
                break
        th.Thread(target=showup).start()
def start():
    canvas.itemconfig(GG,image=none)
    kills.set(0)
    for i in range(10):
        hart_container_list[i].e=hart_list[i][2]
        if hart_container_list[i].e==-1:
            canvas.itemconfig(hart_container_list[i].image,image=none)
        else:
            canvas.itemconfig(hart_container_list[i].image,image=hart)
    canvas.itemconfig(link.image,image=linkwf)
    link.is_alive=1
    canvas.pack()
    #各種會和主角同步的動畫開始!
    th.Thread(target=timer_callback).start()
    #主角出場!
    th.Thread(target=showup).start()
    bord1.place(x=1110,y=10)
    bord2.place(x=1150,y=10)
    pts.pack_forget()
def pause(event):
    global notpaused
    global started
    if started:
        if notpaused==1:
            notpaused=0
            canvas.itemconfig(paused_,image=Paused_image)
        else:
            notpaused=1
            canvas.itemconfig(paused_,image=none)
def gets():
    link.is_alive=0
    canvas.itemconfig(endgame,image=get_sword_image)
    canvas.itemconfig(link.image,image=none)
    th.Timer(3,end).start()
def end():
    global level
    global notpaused
    global started
    canvas.itemconfig(endgame,image=endgame_image)
    pts.pack()
    canvas.pack_forget()
    link.move_to(620,30,'f')
    level=len(monster_move_list)
    next_level()
    started=0
    notpaused=1
###
#創建canvas
canvas=tk.Canvas(root,width=1280,height=660,bg='green')
#套用class
link=main_character(620,-20,linkwf)
for i in monster_list_LV1:
    monster(i[0],i[1],i[2],i[3],i[4])
for i in wall_move_list_LV1:
    wall(i[0],i[1],w1)
for i in wall_static_list:
    wall(i[0], i[1], w)
for i in hart_list:
    hart_container(i[0],i[1],i[2])
###
#新增女神像
sign=canvas.create_image(-500,-500,anchor='center',image=Sign)
endgame=canvas.create_image(-500,-500,anchor='center',image=endgame_image)
###
#新增顯示在螢幕上的變數(主角擊殺數)
kills=tk.IntVar()
kills.set(0)
bord1=tk.Label(root,text='Kill :', bg='green', width=5, height=2 )
bord2=tk.Label(root,textvariable=kills, bg='green', width=3, height=2 )
#起始標籤
pts=tk.Label(root,width=1280,height=650,image=PST_image)
pts.pack()
#暫停標籤
paused_=canvas.create_image(620,300,anchor='center',image=none)
#新增死亡時會出現的[GAMEOVER]字樣
GG=canvas.create_image(620,300,anchor='center',image=none)
###
#GUI綁定鍵盤
root.focus_set()
root.bind('<Key>',callback)
root.bind('<Escape>',pause)
#打包開始遊戲!
root.mainloop()
#關閉所有Thread
os._exit(0)