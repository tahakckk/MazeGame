import turtle
import time
import threading
import random
from functools import partial
from mttkinter import *

number = 2
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Maze Game")
screen.setup(1000,1000)




w,e,n,s = (0,-1),(0,1),(-1,0),(1,0)
quadrants = [[1,1],[-1,1],[-1,-1],[1,-1]]
answers = []
myPen = []
rewards = []
previous = []
temps = [0,0]
finall = 0
for p in range(number):
    previous.append([])
colors = ["orange","cyan"]


text = turtle.Turtle()
text.color('deep pink')
style = ('Courier', 30, 'italic')

text.penup()
text.goto(0,400)
text.pendown()
text.write('Compete with the Computer', font=style, align='center')
text.hideturtle()

text.penup()
text.goto(-230,0)
text.pendown()
text.write('You', font=style, align='center')
text.hideturtle()

text.penup()
text.goto(280,0)
text.pendown()
text.write('Computer', font=style, align='center')
text.hideturtle()

def setupmaze(mainmaze,dic,i):
    treasurecoord = []
    for y in range(len(mainmaze)):
        for x in range(len(mainmaze[y])):
            character = mainmaze[y][x]
            screen_x = -96+(x*24) + quadrants[i][0]*250
            screen_y = 96-(y*24) + quadrants[i][1]*250
            if(character==1):
                pen[i].goto(screen_x,screen_y)
                pen[i].stamp()
            elif(character==0):
                treasurecoord.append([y,x])
    # Treasures
    treasurecoord = random.sample(treasurecoord,5)
    treasurepoint = [-10,-20,-30,-100]
    for element in treasurecoord:
        mainmaze[element[0]][element[1]] = random.choice(treasurepoint)
        screen_x = -96+(element[1]*24)+ quadrants[i][0]*250
        screen_y = 96-(element[0]*24)+ quadrants[i][1]*250
        pen[i].shape("circle")
        pen[i].shapesize(0.5,0.5,0.5)
        pen[i].color("yellow")
        pen[i].goto(screen_x,screen_y)
        dic[tuple(element)]=pen[i].stamp()


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
            text.penup()
            text.goto(+280,-60)
            text.pendown()
            style = ('Courier', 20, 'italic')
            text.write( "Computer got " + str(rewards[k][1]) + " points",font=style, align='center')
            text.penup()
            text.goto(+280,-140)
            text.pendown()
            text.write( "No.of Wrong Ways - " + str(rewards[k][2]),font=style, align='center')
            text.hideturtle()
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
            rewards[k][1] = rewards[k][1] - maze[pos[0]][pos[1]] # Treasure Collected
            pen[k].clearstamp(dic[tuple(pos)])
            pen[k].clearstamp(dic[tuple(pos)])

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
            directions(pos,temp,k)         

def k1(maze,k,direc,dic):
    global temps,finall
    print(k)
    pos = list(map(sum, zip(temps, direc)))    
    lis = []
    try:
        if(maze[pos[0]][pos[1]]<=0 and pos[0]>=0 and pos[1]>=0 and pos[0]<=len(maze)-1 and pos[1]<=len(maze)-1):
            directions(pos,temps,1)
            print(pos,temps)
            temps = pos
            if(pos==[len(maze)-1,len(maze)-1]):
                print(colors[k],"completed")
                print(rewards[k])
                text.penup()
                text.goto(-250,-60)
                text.pendown()
                style = ('Courier', 20, 'italic')
                text.write( "You got " + str(rewards[k][1]) + " points",font=style, align='center')
                text.penup()
                text.goto(-250,-140)
                text.pendown()
                text.write( "No.of Wrong Ways - " + str(rewards[k][2]),font=style, align='center')
                text.hideturtle()
                keys_deactivate()
            if(maze[pos[0]][pos[1]]<0):
                print("Treasure acquired by " + colors[k])
                rewards[k][1] = rewards[k][1] - maze[pos[0]][pos[1]] # Treasure Collected
                pen[k].clearstamp(dic[tuple(pos)])
                pen[k].clearstamp(dic[tuple(pos)])

    except IndexError:
        return
    
def ownmaker(maze,pos,k,dic):
    keys_activate(maze,pos,k,dic)

def keys_activate(maze,pos,k,dic):
    func1 = partial(k1,maze,k,n,dic)
    screen.onkey(func1, "Up")
    func2 = partial(k1,maze,k,w,dic)
    screen.onkey(func2, "Left")
    func3 = partial(k1,maze,k,e,dic)
    screen.onkey(func3, "Right")
    func4 = partial(k1,maze,k,s,dic)
    screen.onkey(func4, "Down")
    screen.listen()

def keys_deactivate():
    screen.onkey(None, 'Up')
    screen.onkey(None, 'Left')
    screen.onkey(None, 'Right')
    screen.onkey(None, 'Down')




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
dic = [{},{}]
for i in range(u):
    rewards.append([i,0,0,0])

t = []
pen = []
mazes = []
for i in range(u):
    pen.append(turtle.Turtle())
    pen[i].shape("square")
    pen[i].color("white")
    pen[i].penup()
    pen[i].speed(0)
    mazes.append([[mainmaze[x][y] for y in range(len(mainmaze[0]))] for x in range(len(mainmaze))])
    setupmaze(mazes[i],dic[i],i)


root = mtTkinter.Tk()

speed = [0,0]



# User - i=0
# AI - i=1
for i in range(u):  
    myPen.append(turtle.Turtle())
    myPen[i].penup() 
    myPen[i].goto(-96+ quadrants[i][0]*250,96+ quadrants[i][1]*250)
    myPen[i].pendown()
    myPen[i].shape('circle')
    myPen[i].color(colors[i])
    myPen[i].fillcolor(colors[i])
    myPen[i].speed(0)
    myPen[i].turtlesize(1,1,1)

t.append(threading.Thread(target=maker,args=(mazes[0],(0,0),0,dic[0],)))
t[0].start()
t.append(threading.Thread(target=ownmaker,args=(mazes[1],(0,0),1,dic[1],)))
t[1].start()


root.mainloop()

for i in range(u):
    t[i].join()

while True:
    pass