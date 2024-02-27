"""
Created on Fri Nov 26 10:04:38 2021

author: Vansh Goenka
"""

 

import random 
import turtle
import math
from tkinter import *
from functools import partial
import tkinter.font as font
from random import randint as rand
                
       
 
def Name(openname):
    openname.destroy()
    openname=Tk()
    openname.geometry("400X400")
    openname.title("Menu")
    

def startgame(startg):
    startg.destroy()
    windowtur=turtle.Screen()
    windowtur.bgcolor("#051e3e")
    windowtur.title("Maza-thon")
    windowtur.setup(1920,1080)
    windowtur.tracer(0)
    #register shapes
    req_images=["main_character.gif","wall.gif",
                "main_character.gif","tres2.gif","enemy_left.gif",
                "enemy_right.gif"]
    
    for image in req_images:
        turtle.register_shape(image)
    class Pen(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.penup()
            self.speed(0)
            
    class Player(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("main_character.gif")
            self.color("red")
            self.penup()
            self.speed(0)
            self.gold=0
        def goup(self):
            xx=self.xcor()
            yy=self.ycor()+24        
            if (xx,yy) not in walls:
                self.goto(xx,yy)
        def godown(self):
            xx=player.xcor()
            yy=player.ycor()-24        
            if (xx,yy) not in walls:
                self.goto(xx,yy)
        def goleft(self):
            xx=player.xcor()-24
            yy=player.ycor()    
            self.shape("main_character.gif")
            if (xx,yy) not in walls:
                self.goto(xx,yy)
        def goright(self):
            xx=player.xcor()+24
            yy=player.ycor()   
            self.shape("main_character.gif")
            if (xx,yy) not in walls:
                self.goto(xx,yy)
                
        def is_coll(self,other):
            a=self.xcor()-other.xcor()
            b=self.ycor()-other.ycor()
            dist=math.sqrt((a**2)+(b**2))
            if dist==0:
                return True
            else:
                return False
    class Treasure(turtle.Turtle):
        def __init__(self,x,y):
            turtle.Turtle.__init__(self)
            self.shape("tres2.gif")
            #self.color("gold")
            self.penup()
            self.speed(0)
            self.gold=1000
            self.goto(x,y)
            
        def destroy(self):
            self.goto(2000,2000)
            self.hideturtle()
            
    class Enemy(turtle.Turtle):
        def __init__(self,x,y):
            turtle.Turtle.__init__(self)
            self.shape("enemy_left.gif")
            #self.color("gold")
            self.penup()
            self.speed(0)
            self.gold=1000
            self.goto(x,y)
            self.direction=random.choice(["up","down",
                                          "left","right"])
            
        def move(self):
            if self.direction=="up":
                dx=0
                dy=24
            elif self.direction=="down":
                dx=0
                dy=-24
            elif self.direction=="left":
                dx=-24
                dy=0
                self.shape("enemy_left.gif")
            elif self.direction=="right":           
                dx=24
                dy=0
                self.shape("enemy_right.gif")
            else:
                dx=0
                dy=0
          
            if self.is_close(player):
                if player.xcor()<self.xcor():
                    self.direction="left"
                elif player.xcor()>self.xcor():
                    self.direction="right"
                elif player.ycor()<self.ycor():
                    self.direction="down"
                elif player.ycor()>self.ycor():
                    self.direction="up"
                    
            xx=self.xcor()+dx
            yy=self.ycor()+dy
        
            if(xx,yy) not in walls:
                self.goto(xx,yy)
            else:
                self.direction=random.choice(["up","down",
                                              "left","right"])
            
            turtle.ontimer(self.move,t=random.randint(100,500))
        def is_close(self,other):
            a=self.xcor()-other.xcor()
            b=self.ycor()-other.ycor()
            dist=math.sqrt((a**2)+(b**2))
            
            if dist <75:
                return True
            else:
                return False
      
       
            
    levels=[""]
    
    level_1=[
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXX     XXXX  EXXXXXXX",
    "X  XXXXXX             XXX",
    "X  XX     XXXXXXXXX  XXXX",
    "X TXX  XXXXXXTXXXXX  XXXX",
    "X      XXXXX  XXXXX    XX",
    "XXX  XXXXXXX  XXXXX  XXXX",
    "XXE  XXX     EXXX  X XXXX",
    "X    XXXE            XXXX",
    "XXX  XXXXXXXXXXXXXX     X",
    "XXX                  XXXX",
    "XXX  XXXX  XXXXXXXXXXX TX",
    "XXXXXXXXX  XXXX  X      X",
    "XXXXXXXXX  XXXX  X  XXXXX",
    "X          XXXX       XXX",
    "X  XXXXXX  XX    XX  XXXX",
    "X  XX  XXXXXXXX  XX  XXXX",
    "X  XX  XXXXXXXX  XXXXXXXX",
    "X        X            EXX",
    "XXXXX  XXXXXXXXXXXXXX  XX",
    "XE                XXX  XX",
    "X  XXXXXXXX   XXX   XX XX",
    "X  XXXXXXXX X XXX X XX XX",
    "XXXE        XT    X    XX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
    ]
    
    treasures=[]
    
    levels.append(level_1)
    def set_maze(level):
        for y in range(len(level)):
            for x in range(len(level[y])):
                #get character at each x,y coordinate 
                # NOTE the order of y and x in the next line
                character=level[y][x]
                #calculate the screen x,y coordinate
                screen_x=-288+(x*24)
                screen_y= 288-(y*24)
                
                #check if it is an x(reprsenting a wall)
                if character =="X":
                    pen.goto(screen_x,screen_y)
                    pen.shape("wall.gif")
                    pen.stamp()                 
                    walls.append((screen_x,screen_y))
                if character =="P":
                    player.goto(screen_x,screen_y)
                if character=="T":
                    treasures.append(Treasure(screen_x,screen_y))
                if character=="E":
                    enemies.append(Enemy(screen_x,screen_y))
    #create class instances
    pen=Pen()
    player=Player()
    walls=[]
    enemies=[]
    #set up the level
    set_maze(levels[1])
    
    
     
    turtle.listen()
    turtle.onkey(player.goleft,"Left")
    turtle.onkey(player.goright,"Right")
    turtle.onkey(player.goup,"Up")
    turtle.onkey(player.godown,"Down")     
    
     
    windowtur.tracer(0)
    
     
    for en in enemies:
        turtle.ontimer(en.move,t=250)
    
    x=0
    while True:
        for treasure in treasures:
            if player.is_coll(treasure):
                #add the treasure gold to the player gold
                player.gold+=treasure.gold
                print("Gold:{}".format(player.gold))
                treasure.destroy()
                score_pen=turtle.Turtle()
                score_pen.speed(0)
                score_pen.color("white")
                score_pen.penup()
                score_pen.setposition(-290,310)
                scorestring="Score: %s" % player.gold
                score_pen.write(scorestring,False,align="left",font=("Arial",25,"bold"))
                 
        
        for en in enemies:
            if player.is_coll(en):
                print("player dies!")  
                x+=1
        if x==5:
            windowtur.bye()
            gameover=Tk()
            gameover.title("You Lose")
            gohome=partial(menu)
            gameover.geometry("400x400")
            canvas=Canvas(gameover,width=400,height=400)
            canvas.pack()
            img = PhotoImage(file="Game_over.png")               
            canvas.create_image(40,40, anchor=NW, image=img)              
            gameover.mainloop()
        windowtur.update()
 
def sel(): 
    selection=[]
    select="you selected set "+str(var.get())
    selection.append(select)
    for i in range(len(selection)):
        label.config(text=selection[i])
        label.pack()
    
def Controls(changecon):
    changecon.destroy()
    changecon=Tk()
    global var
    var=IntVar()
    changecon.title("Controls")
    r1=Radiobutton(changecon,fg="blue",width=20,height=20,text="Set 1\nw,a,s,d",variable=var,value=1,command=sel)
    r2=Radiobutton(changecon,text="Set 2\n Arrow Keys",width=20,height=20,
                   fg="blue",value=2,variable=var,command=sel)
    r1.pack(anchor=W)
    r2.pack(anchor=W)
    global label
    label=Label(changecon)
   
def Settings(opensett):
    opensett.destroy()
    opensett=Tk()
    opensett.title("Settings")
    cc=partial(Controls,opensett)
    bgchange=Button(opensett,text="Change Background",width=30,height=3,activeforeground = 'red', 
                activebackground = "yellow",bg="orange",fg="blue")
    lead=Button(opensett,text="Leaderboard",width=30,height=3,activeforeground = 'red', 
                activebackground = "yellow",bg="orange",fg="blue")
    cont=Button(opensett,text="Controls",width=30,height=3,activeforeground = 'red', 
                activebackground = "yellow",bg="orange",fg="blue",command=cc)
    #controls
    lead.pack()
    bgchange.pack()
    cont.pack() 
        
    #exit the game/window
def Exit(openexit):
    openexit.destroy()
    
def bosskey():
    boss=Tk()
    boss.title("")
    canvas=Canvas(boss,width=400,height=400)
    
#Main menu
def menu():
    window=Tk()
    window.title("MENU")
    window.geometry("450x330")
    start=partial(startgame,window)
    settings=partial(Settings,window)
    name=partial(Name,window)
    exitt=partial(Exit,window)
    name=Button(window,text="MAZAA-THON",command="name",fg = "red",bg="#fbf9f6",width = 50,state=DISABLED,height=3,font = "Arial 20", bd = None)
    name.pack()
    play = Button(window, text = "Start", command=start,
                activeforeground = 'red', 
                activebackground = "yellow", bg = "orange", 
                fg = "blue", width = 50,height=2, font = 'Arial 16', bd = 4) 
    play.pack(side="top")
    sett = Button(window, text = "Settings", command=settings,
                activeforeground = 'red', 
                activebackground = "yellow", bg = "orange", 
                fg = "blue", width = 50,height=2,font = 'Arial 16', bd = 4) 
    sett.pack(side="top")
    exitt = Button(window, text = "Quit", command=exitt,
                activeforeground = 'red', 
                activebackground = "yellow", bg = "orange", 
                fg = "blue", width = 50,height=2, font = 'Arial 16', bd = 4) 
    exitt.pack(side="top")    
    button=Button()     
    window.mainloop()     
     

if __name__=="__main__"   :
    menu() 

            

        
        
