import turtle
import time
import threading
from threading import Semaphore
import random
from mttkinter import *

number = 4
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Maze Game")
screen.setup(500,500)
w,e,n,s = (0,-1),(0,1),(-1,0),(1,0)
quadrants = [[1,1],[-1,1],[-1,-1],[1,-1]]
answers = []
myPen = []
rewards = []
previous = []
for p in range(number):
    previous.append([])
colors = ["blue","green","orange","cyan"]

def setupmaze(mainmaze,dic):
    treasurecoord = []
    for y in range(len(mainmaze)):
        for x in range(len(mainmaze[y])):
            character = mainmaze[y][x]
            screen_x = -96+(x*24)
            screen_y = 96-(y*24)
            if(character==1):
                pen.goto(screen_x,screen_y)
                pen.stamp()
            elif(character==0):
                treasurecoord.append([y,x])
    # Treasures
    treasurecoord = random.sample(treasurecoord,5)
    print(treasurecoord)
    treasurepoint = [-10,-20,-30,-100]
    for element in treasurecoord:
        mainmaze[element[0]][element[1]] = random.choice(treasurepoint)
        print(mainmaze[element[0]][element[1]])
        screen_x = -96+(element[1]*24)
        screen_y = 96-(element[0]*24)
        treasure.shape("circle")
        treasure.shapesize(0.5,0.5,0.5)
        treasure.color("yellow")
        treasure.goto(screen_x,screen_y)
        dic[tuple(element)]=treasure.stamp()


def directions(pos,temp,k):
    if(pos[0]-temp[0]!=0):
        if(pos[0]-temp[0]>0):
            myPen[k].right(90)
            myPen[k].forward(24)
            myPen[k].left(90)
        else:
            myPen[k].left(90)
            myPen[k].forward(24)
            myPen[k].right(90)
    elif(pos[1]-temp[1]!=0):
        if(pos[1]-temp[1]>0):
            myPen[k].forward(24)
        else:
            myPen[k].left(90)
            myPen[k].left(90)
            myPen[k].forward(24)
            myPen[k].right(90)
            myPen[k].right(90)

def maker(maze,pos,k,dic):
    check=0
    while(True):
        north = tuple(map(sum, zip(pos, n)))
        south = tuple(map(sum, zip(pos, s)))
        west = tuple(map(sum, zip(pos, w)))    
        east = tuple(map(sum, zip(pos, e)))

        if(pos==(len(maze)-1,len(maze)-1)):
            print(colors[k],"completed")
            maze[pos[0]][pos[1]] = 9     
            answers.append(maze)
            print(rewards[k])
            return
        lis = []

        try:
            if(maze[north[0]][north[1]]<=0 and north[0]>=0 and north[1]>=0):
                lis.append(north)
        except IndexError:
            pass

        try:
            if(maze[south[0]][south[1]]<=0 and south[0]>=0 and south[1]>=0):
                lis.append(south)
        except IndexError:
            pass

        try:
            if(maze[west[0]][west[1]]<=0 and west[0]>=0 and west[1]>=0):
                lis.append(west)
        except IndexError:
            pass

        try:
            if(maze[east[0]][east[1]]<=0 and east[0]>=0 and east[1]>=0):
                lis.append(east)
        except IndexError:
            pass

        if(maze[pos[0]][pos[1]]<0):
            print("Treasure acquired by " + colors[k])
            time.sleep(1)
            sem[pos].release()            

        if(len(lis)==0):
            maze[pos[0]][pos[1]] = 2
            try:
                temp = pos
                pos = previous[k][-1]
                if(check==0):
                    print("A Wrong Way",colors[k])
                    rewards[k][1] = rewards[k][1] - 10
                    rewards[k][2] = rewards[k][2] + 1
                    myPen[k].turtlesize(1.5,1.5,1.5)
                    myPen[k].color("red")
                    time.sleep(2)
                    myPen[k].color(colors[k])
                    myPen[k].turtlesize(1,1,1)
                directions(pos,temp,k)
                check+=1
                previous[k].pop()
            except IndexError:
                print("No way possible")
                return

        else:
            check=0
            previous[k].append(pos)

            maze[pos[0]][pos[1]] = 9        
            temp = pos      
            pos = random.choice(lis)
            if(maze[pos[0]][pos[1]]<0):
                if(sem[pos]._value==0):
                    print(colors[k],"is waiting")
                sem[pos].acquire()
                rewards[k][1] = rewards[k][1] - maze[pos[0]][pos[1]] # Treasure Collected
            directions(pos,temp,k)         
            
mainmaze = [[0,0,1,1,1,1,1,1,1,1,1],
            [1,0,0,1,1,0,0,0,1,1,1],
            [1,1,0,0,0,0,1,0,0,1,1],
            [1,0,0,1,1,1,1,1,0,1,1],
            [1,1,0,0,1,0,0,0,0,1,1],
            [1,1,1,0,1,0,1,0,0,1,1],
            [1,1,1,0,0,0,1,1,0,1,1],
            [1,1,1,1,1,0,0,1,0,1,1],
            [1,1,1,1,1,1,0,0,0,1,1],
            [1,1,1,1,1,1,1,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,0,0]]

u = number
dic = {}
for i in range(u):
    rewards.append([i,0,0,0])

t = []
treasure=turtle.Turtle()
treasure.penup()
pen = turtle.Turtle()
pen.shape("square")
pen.color("white")
pen.penup()
pen.speed(3)
setupmaze(mainmaze,dic)
print(dic)

sem = dic
for key in dic:
    sem[key] = Semaphore()
print(sem)
mazes = []
for i in range(number):
    mazes.append([[mainmaze[x][y] for y in range(len(mainmaze[0]))] for x in range(len(mainmaze))])


root = mtTkinter.Tk()

for i in range(u):  
    myPen.append(turtle.Turtle())
    myPen[i].penup() 
    myPen[i].goto(-96,96)
    myPen[i].shape('circle')
    myPen[i].color(colors[i])
    myPen[i].fillcolor(colors[i])
    myPen[i].speed(3)
    myPen[i].turtlesize(1,1,1)
    myPen[i].pendown()


for i in range(u):  
    t.append(threading.Thread(target=maker,args=(mazes[i],(0,0),i,dic,)))
    t[i].start()

root.mainloop()

for i in range(u):
    t[i].join()

for i in range(len(rewards)):
    print("Player:",i+1)
    print()    
    print("No.of wrong ways faced :", rewards[i][2])
    print("Score :", rewards[i][1])
    print()

while True:
    pass