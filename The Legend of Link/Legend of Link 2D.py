import tkinter as tk
import threading as th
from subprocess import call
from random import randint, choice

root=tk.Tk()
root.title('The Legend of Zelda')
root.geometry('1280x650')
canvas=tk.Canvas(root,width=1280,height=660,bg='green')
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
ganon1=tk.PhotoImage(file='gameobject\\ganon1.gif')
ganon2=tk.PhotoImage(file='gameobject\\ganon2.gif')
ganon=tk.PhotoImage(file='gameobject\\ganon.gif')
hart=tk.PhotoImage(file='gameobject\\hart.gif')
hart0=tk.PhotoImage(file='gameobject\\hart_black.gif')
none=tk.PhotoImage(file='gameobject\\hart0.gif')
w=tk.PhotoImage(file='gameobject\\wall.gif')
w1=tk.PhotoImage(file='gameobject\\wall1.gif')
tir_force=tk.PhotoImage(file='gameobject\\Triforce_Artwork.gif')
gameover=tk.PhotoImage(file='gameobject\\gameover.gif')
Sign=tk.PhotoImage(file='gameobject\\sign.gif')
logo=tk.PhotoImage(file='gameobject\\logo.gif')
root.tk.call('wm', 'iconphoto', root._w, logo)
Tri=canvas.create_image(620,300,anchor='center',image=tir_force)
hart_list=[[255,30,-1],[230,30,-1],[205,30,-1],[180,30,-1],
[155,30,-1],[130,30,-1],[105,30,-1],[80,30,1],[55,30,1],[30,30,1]]
monster_list=[[420,500,-5,1,1],[420,100,-5,1,1],[820,500,5,1,1],[820,100,5,1,1]]
wall_list_w=[
[-1330,-1200],[-1280,-1200],[-1230,-1200],[-1180,-1200],
[-1130,-1200],[-1080,-1200],[-1030,-1200],[-980,-1200],
[-930,-1200],[-880,-1200],[-680,-1200],[-630,-1200],[-580,-1200],
[-530,-1200],[-480,-1200],[-430,-1200],[-380,-1200],
[-330,-1200],[-280,-1200],[-230,-1200],[-180,-1200],
[20,-1200],
[70,-1200],[120,-1200],[170,-1200],[220,-1200],
[270,-1200],[320,-1200],[370,-1200],[420,-1200],
[470,-1200],[520,-1200],[720,-1200],[770,-1200],[820,-1200],
[870,-1200],[920,-1200],[970,-1200],[1020,-1200],
[1070,-1200],[1120,-1200],[1170,-1200],[1220,-1200],
[1420,-1200],
[1470,-1200],[1520,-1200],[1570,-1200],[1620,-1200],
[1670,-1200],[1720,-1200],[1770,-1200],[1820,-1200],
[1870,-1200],[1920,-1200],[1970,-1200],[2120,-1200],[2170,-1200],[2220,-1200],
[2270,-1200],[2320,-1200],[2370,-1200],[-1330,-600],
[-1280,-600],[-1230,-600],[-1180,-600],[-1130,-600],
[-1080,-600],[-1030,-600],[-980,-600],[-930,-600],
[-880,-600],[-680,-600],[-630,-600],[-580,-600],[-530,-600],
[-480,-600],[-430,-600],[-380,-600],[-330,-600],
[-280,-600],[-230,-600],[-180,-600],[20,-600],[70,-600],
[120,-600],[170,-600],[220,-600],[270,-600],
[320,-600],[370,-600],[420,-600],[470,-600],
[520,-600],[720,-600],[770,-600],[820,-600],[870,-600],
[920,-600],[970,-600],[1020,-600],[1070,-600],
[1120,-600],[1170,-600],[1220,-600],[1420,-600],[1470,-600],
[1520,-600],[1570,-600],[1620,-600],[1670,-600],
[1720,-600],[1770,-600],[1820,-600],[1870,-600],
[1920,-600],[1970,-600],[2120,-600],[2170,-600],[2220,-600],[2270,-600],
[2320,-600],[2370,-600],[-1330,0],[-1280,0],
[-1230,0],[-1180,0],[-1130,0],[-1080,0],
[-1030,0],[-980,0],[-930,0],[-880,0],
[-680,0],
[-630,0],[-580,0],[-530,0],[-480,0],
[-430,0],[-380,0],[-330,0],[-280,0],
[-230,0],[-180,0],[20,0],[70,0],[120,0],
[170,0],[220,0],[270,0],[320,0],
[370,0],[420,0],[470,0],[520,0],
[720,0],
[770,0],[820,0],[870,0],[920,0],
[970,0],[1020,0],[1070,0],[1120,0],
[1170,0],[1220,0],[1420,0],[1470,0],[1520,0],
[1570,0],[1620,0],[1670,0],[1720,0],
[1770,0],[1820,0],[1870,0],[1920,0],
[1970,0],[2120,0],
[2170,0],[2220,0],[2270,0],[2320,0],
[2370,0],[-1330,600],[-1280,600],[-1230,600],
[-1180,600],[-1130,600],[-1080,600],[-1030,600],
[-980,600],[-930,600],[-880,600],[-680,600],[-630,600],
[-580,600],[-530,600],[-480,600],[-430,600],
[-380,600],[-330,600],[-280,600],[-230,600],
[-180,600],[20,600],[70,600],[120,600],[170,600],
[220,600],[270,600],[320,600],[370,600],
[420,600],[470,600],[520,600],[720,600],[770,600],
[820,600],[870,600],[920,600],[970,600],
[1020,600],[1070,600],[1120,600],[1170,600],
[1220,600],[1420,600],[1470,600],[1520,600],[1570,600],
[1620,600],[1670,600],[1720,600],[1770,600],
[1820,600],[1870,600],[1920,600],[1970,600],
[2120,600],[2170,600],
[2220,600],[2270,600],[2320,600],[2370,600],
[-1330,1200],[-1280,1200],[-1230,1200],[-1180,1200],
[-1130,1200],[-1080,1200],[-1030,1200],[-980,1200],
[-930,1200],[-880,1200],[-680,1200],[-630,1200],[-580,1200],
[-530,1200],[-480,1200],[-430,1200],[-380,1200],
[-330,1200],[-280,1200],[-230,1200],[-180,1200],
[20,1200],
[70,1200],[120,1200],[170,1200],[220,1200],
[270,1200],[320,1200],[370,1200],[420,1200],
[470,1200],[520,1200],[720,1200],[770,1200],[820,1200],
[870,1200],[920,1200],[970,1200],[1020,1200],
[1070,1200],[1120,1200],[1170,1200],[1220,1200],
[1420,1200],
[1470,1200],[1520,1200],[1570,1200],[1620,1200],
[1670,1200],[1720,1200],[1770,1200],[1820,1200],
[1870,1200],[1920,1200],[1970,1200],[2120,1200],[2170,1200],[2220,1200],
[2270,1200],[2320,1200],[2370,1200],[-1330,1800],
[-1280,1800],[-1230,1800],[-1180,1800],[-1130,1800],
[-1080,1800],[-1030,1800],[-980,1800],[-930,1800],
[-880,1800],[-680,1800],[-630,1800],[-580,1800],[-530,1800],
[-480,1800],[-430,1800],[-380,1800],[-330,1800],
[-280,1800],[-230,1800],[-180,1800],[20,1800],[70,1800],
[120,1800],[170,1800],[220,1800],[270,1800],
[320,1800],[370,1800],[420,1800],[470,1800],
[520,1800],[720,1800],[770,1800],[820,1800],[870,1800],
[920,1800],[970,1800],[1020,1800],[1070,1800],
[1120,1800],[1170,1800],[1220,1800],[1420,1800],[1470,1800],
[1520,1800],[1570,1800],[1620,1800],[1670,1800],
[1720,1800],[1770,1800],[1820,1800],[1870,1800],
[1920,1800],[1970,1800],[2120,1800],[2170,1800],[2220,1800],[2270,1800],
[2320,1800],[2370,1800],
###
[-1130,-1200],[-1130,-1150],[-1130,-1100],[-1130,-1050],
[-1130,-1000],[-1130,-850],
[-1130,-800],[-1130,-750],[-1130,-700],[-1130,-650],
[-1130,-600],[-1130,-550],[-1130,-500],[-1130,-450],
[-1130,-400],[-1130,-200],[-1130,-150],[-1130,-100],[-1130,-50],
[-1130,0],[-1130,50],[-1130,100],[-1130,150],
[-1130,200],[-1130,400],[-1130,450],[-1130,500],[-1130,550],
[-1130,600],[-1130,650],[-1130,700],[-1130,750],
[-1130,800],[-1130,1000],[-1130,1050],[-1130,1100],[-1130,1150],
[-1130,1200],[-1130,1250],[-1130,1300],[-1130,1350],
[-1130,1400],[-1130,1600],[-1130,1650],[-1130,1700],[-1130,1750],
[-1130,1800],[-1130,1850],[-1130,1900],[-1130,1950],
[-1130,2000],[-1130,2200],[-1130,2250],[-1130,2300],[-1130,2350],
[-430,-1200],[-430,-1150],[-430,-1100],[-430,-1050],
[-430,-1000],[-430,-850],
[-430,-800],[-430,-750],[-430,-700],[-430,-650],
[-430,-600],[-430,-550],[-430,-500],[-430,-450],
[-430,-400],[-430,-200],[-430,-150],[-430,-100],[-430,-50],
[-430,0],[-430,50],[-430,100],[-430,150],
[-430,200],[-430,400],[-430,450],[-430,500],[-430,550],
[-430,600],[-430,650],[-430,700],[-430,750],
[-430,800],[-430,1000],[-430,1050],[-430,1100],[-430,1150],
[-430,1200],[-430,1250],[-430,1300],[-430,1350],
[-430,1400],[-430,1600],[-430,1650],[-430,1700],[-430,1750],
[-430,1800],[-430,1850],[-430,1900],[-430,1950],
[-430,2000],[-430,2200],[-430,2250],[-430,2300],[-430,2350],
[270,-1200],[270,-1150],[270,-1100],[270,-1050],
[270,-1000],[270,-850],
[270,-800],[270,-750],[270,-700],[270,-650],
[270,-600],[270,-550],[270,-500],[270,-450],
[270,-400],[270,-200],[270,-150],[270,-100],[270,-50],
[270,0],[270,50],[270,100],[270,150],
[270,200],[270,400],[270,450],[270,500],[270,550],
[270,600],[270,650],[270,700],[270,750],
[270,800],[270,1000],[270,1050],[270,1100],[270,1150],
[270,1200],[270,1250],[270,1300],[270,1350],
[270,1400],[270,1600],[270,1650],[270,1700],[270,1750],
[270,1800],[270,1850],[270,1900],[270,1950],
[270,2000],[270,2200],[270,2250],[270,2300],[270,2350],
[970,-1200],[970,-1150],[970,-1100],[970,-1050],
[970,-1000],[970,-850],
[970,-800],[970,-750],[970,-700],[970,-650],
[970,-600],[970,-550],[970,-500],[970,-450],
[970,-400],[970,-200],[970,-150],[970,-100],[970,-50],
[970,0],[970,50],[970,100],[970,150],
[970,200],[970,400],[970,450],[970,500],[970,550],
[970,600],[970,650],[970,700],[970,750],
[970,800],[970,1000],[970,1050],[970,1100],[970,1150],
[970,1200],[970,1250],[970,1300],[970,1350],
[970,1400],[970,1600],[970,1650],[970,1700],[970,1750],
[970,1800],[970,1850],[970,1900],[970,1950],
[970,2000],[970,2200],[970,2250],[970,2300],[970,2350],
[1670,-1200],[1670,-1150],[1670,-1100],[1670,-1050],
[1670,-1000],[1670,-850],
[1670,-800],[1670,-750],[1670,-700],[1670,-650],
[1670,-600],[1670,-550],[1670,-500],[1670,-450],
[1670,-400],[1670,-200],[1670,-150],[1670,-100],[1670,-50],
[1670,0],[1670,50],[1670,100],[1670,150],
[1670,200],[1670,400],[1670,450],[1670,500],[1670,550],
[1670,600],[1670,650],[1670,700],[1670,750],
[1670,800],[1670,1000],[1670,1050],[1670,1100],[1670,1150],
[1670,1200],[1670,1250],[1670,1300],[1670,1350],
[1670,1400],[1670,1600],[1670,1650],[1670,1700],[1670,1750],
[1670,1800],[1670,1850],[1670,1900],[1670,1950],
[1670,2000],[1670,2200],[1670,2250],[1670,2300],[1670,2350],
###
[420,450,-5,1,1],[420,150,-5,1,1],[820,450,5,1,1],[820,150,5,1,1]
]
monster__list=[]
wall__list=[]
hart_container_list=[]
class main_character():
    def __init__(self,name,x,y,imag):
        self.kill=0
        self.is_alive=True
        self.name=name
        self.image= canvas.create_image(x,y,anchor='center',image=imag)
        self.dire='f'
        self.attack='c'
        self.lives='3'
        self.level=1

    def delete(self):
        self.is_alive=False
        canvas.itemconfig(self.image,image=none)

    def walk(self,code):
        if self.is_alive==True:
            if chr(code)=='A' or chr(code)=='a':
                canvas.itemconfig(link.image, image = linkwl)
                self.dire='l'
                canvas.move(Tri,5,0)
                for i in wall__list:
                    canvas.move(i.image,5,0)
                for i in monster__list:
                    canvas.move(i.image,5,0)

            if chr(code)=='D' or chr(code)=='d':
                canvas.itemconfig(link.image, image = linkwr)
                self.dire='r'
                canvas.move(Tri,-5,0)
                for i in wall__list:
                    canvas.move(i.image,-5,0)
                for i in monster__list:
                    canvas.move(i.image,-5,0)

            if chr(code)=='W' or chr(code)=='w':
                canvas.itemconfig(link.image, image = linkwb)
                self.dire='b'
                canvas.move(Tri,0,5)
                for i in wall__list:
                    canvas.move(i.image,0,5)
                for i in monster__list:
                    canvas.move(i.image,0,5)

            if chr(code)=='S' or chr(code)=='s':
                canvas.itemconfig(link.image, image = linkwf)
                self.dire='f'
                canvas.move(Tri,0,-5)
                for i in wall__list:
                    canvas.move(i.image,0,-5)
                for i in monster__list:
                    canvas.move(i.image,0,-5)

            if code==32:
                if self.dire=='f':
                    canvas.itemconfig(link.image, image = linkf)
                    self.attack='f'
                    th.Timer(0.3,back_to_stand).start()
                if self.dire=='l':
                    canvas.itemconfig(link.image, image = linkl)
                    self.attack='l'
                    th.Timer(0.3,back_to_stand).start()
                if self.dire=='r':
                    canvas.itemconfig(link.image, image = linkr)
                    self.attack='r'
                    th.Timer(0.3,back_to_stand).start()
                if self.dire=='b':
                    canvas.itemconfig(link.image, image = linkb)
                    self.attack='b'
                    th.Timer(0.3,back_to_stand).start()
            for i in wall__list:
                i.block(code)

    def is_hurt(self,code,move):
        if chr(code)=='A' or chr(code)=='a':
            canvas.move(Tri,-move,0)
            for i in wall__list:
                canvas.move(i.image,-move,0)
            for i in monster__list:
                canvas.move(i.image,-move,0)
        if chr(code)=='D' or chr(code)=='d':
            canvas.move(Tri,move,0)
            for i in wall__list:
                canvas.move(i.image,move,0)
            for i in monster__list:
                canvas.move(i.image,move,0)
        if chr(code)=='W' or chr(code)=='w':
            canvas.move(Tri,0,-move)
            for i in wall__list:
                canvas.move(i.image,0,-move)
            for i in monster__list:
                canvas.move(i.image,0,-move)
        if chr(code)=='S' or chr(code)=='s':
            canvas.move(Tri,0,move)
            for i in wall__list:
                canvas.move(i.image,0,move)
            for i in monster__list:
                canvas.move(i.image,0,move)


class monster():
    def __init__(self,x,y,step,dire,lives):
        self.image=canvas.create_image(x,y,anchor='center',image=mon)
        self.step = step
        self.dire=dire
        self.x=x
        self.y=y
        self.die_count=0
        self.lives=lives
        self.count_step=0
        monster__list.append(self)

    def delete(self):
        th.Timer(0.03,self.die_config).start()
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
                    self.count_step+=1
                    if self.count_step==12:
                        self.count_step=0
                        self.step = -self.step
            if self.dire==2:
                if canvas.coords(self.image):
                    canvas.move(self.image,0,self.step)
                    self.count_step+=1
                    if self.count_step==12:
                        self.count_step=0
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
                        canvas.itemconfig(i,image=hart0)
                        link.delete()
                        #canvas.itemconfig(GG,image=gameover)

                    
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
                        rubby.set(rubby.get() + 1)
                        link.kill+=1

    def die_config(self):
        if self.die_count%2==1:
            canvas.itemconfig(self.image,image=none)
        if self.die_count%2==0:
            canvas.itemconfig(self.image,image=mon)
        if self.die_count<=10:
            self.die_count+=1
            th.Timer(0.03,self.die_config).start()

class hart_container():
    def __init__(self,x,y,e):
        hart_container_list.append(self)
        self.e=e
        if e==-1:
            self.image=canvas.create_image(x,y,anchor='center',image=none)
        else:
            self.image=canvas.create_image(x,y,anchor='center',image=hart)

class wall():
    def __init__(self,x,y,img):
        self.image=canvas.create_image(x,y,anchor='center',image=img)
        wall__list.append(self)
    def block(self,code):
        if canvas.coords(link.image):
            if abs(canvas.coords(link.image)[0] - canvas.coords(self.image)[0]) < 45 and abs(canvas.coords(link.image)[1] - canvas.coords(self.image)[1])<45:
                    link.is_hurt(code,5)
def callback(event):
    link.walk(event.keycode)
    for i in monster__list:
        i.is_dead_or_not(event.keycode)

def timer_callback():
    for i in monster__list:
        i.move()
        i.can_attack_or_not()
    th.Timer(0.05, timer_callback).start()
for i in wall_list_w:
    wall(i[0], i[1], w)
for i in hart_list:
    hart_container(i[0],i[1],i[2])
for i in monster_list:
    monster(i[0],i[1],i[2],i[3],i[4])
link=main_character('link',620,300,linkwf)
rubby=tk.IntVar()
rubby.set(link.kill)
tk.Label(root,text='Kill :', bg='green', width=5, height=2 ).place(x=1110,y=10)
tk.Label(root,textvariable=rubby, bg='green', width=3, height=2 ).place(x=1150,y=10)

def back_to_stand():
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

t=th.Timer(0.05,timer_callback)
t.start()
canvas.focus_set()
canvas.bind('<Key>',callback)
canvas.pack()
root.mainloop()