import turtle
import time
import random


screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Maze Game")
screen.setup(500,500)
w,e,n,s = (0,-1),(0,1),(-1,0),(1,0)
previous = []
answers = []
rewards = []


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


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

    treasurecoord = random.sample(treasurecoord,5)
    treasurepoint = [-10,-20,-30,-100]
    for element in treasurecoord:
        mainmaze[element[0]][element[1]] = random.choice(treasurepoint)
        screen_x = -96+(element[1]*24)
        screen_y = 96-(element[0]*24)
        pen.shape("circle")
        pen.shapesize(0.5,0.5,0.5)
        pen.color("yellow")
        pen.goto(screen_x,screen_y)
        dic[tuple(element)]=pen.stamp()


def directions(pos,temp):
    if(pos[0]-temp[0]!=0):
        if(pos[0]-temp[0]>0):
            myPen.right(90)
            myPen.forward(24)
            myPen.left(90)
        else:
            myPen.left(90)
            myPen.forward(24)
            myPen.right(90)
    elif(pos[1]-temp[1]!=0):
        if(pos[1]-temp[1]>0):
            myPen.forward(24)
        else:
            myPen.left(90)
            myPen.left(90)
            myPen.forward(24)
            myPen.right(90)
            myPen.right(90)


def maker(maze,pos,k,dic):
    check=0
    while(True):
        north = tuple(map(sum, zip(pos, n)))
        south = tuple(map(sum, zip(pos, s)))
        west = tuple(map(sum, zip(pos, w)))    
        east = tuple(map(sum, zip(pos, e)))

        if(pos==(len(maze)-1,len(maze)-1)):
            maze[pos[0]][pos[1]] = 9     
            answers.append(maze)
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

        if(mainmaze[pos[0]][pos[1]]<0):
            rewards[k][1] = rewards[k][1] - mainmaze[pos[0]][pos[1]] # Treasure Collected
            pen.clearstamp(dic[tuple(pos)])
            

        if(len(lis)==0):
            maze[pos[0]][pos[1]] = 2
            try:
                temp = pos
                pos = previous[-1]
                if(check==0):
                    rewards[k][1] = rewards[k][1] - 5
                    rewards[k][2] = rewards[k][2] + 1
                    myPen.turtlesize(1.5,1.5,1.5)
                    myPen.color("red")
                    time.sleep(2)
                    myPen.color("pink")
                    myPen.turtlesize(1,1,1)
                directions(pos,temp)
                check+=1
                previous.pop()
            except IndexError:
                print("No way possible")
                return

        else:
            check=0
            previous.append(pos)
            maze[pos[0]][pos[1]] = 9        
            temp = pos      
            pos = random.choice(lis)
            directions(pos,temp)
            

            
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


u = 1
dic = {}
for i in range(u):
    rewards.append([i,0,0,0])
myPen=turtle.Turtle()

pen = Pen()
setupmaze(mainmaze,dic)
myPen.penup() 
myPen.goto(-96,96)
myPen.pendown()
myPen.shape('circle')
myPen.color("pink")
myPen.up()
myPen.speed(1)
myPen.turtlesize(1,1,1)
maker(mainmaze,(0,0),0,dic)


for i,answer in enumerate(answers):
    print("Player:",i+1)
    print()
    for row in answer:
        print(row)
    print()    
    print("Wrong Way :", rewards[i][2])
    print("Score :", rewards[i][1])
    print()


while True:
    pass