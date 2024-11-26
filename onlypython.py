import threading
import matplotlib.pyplot as plt
import random
w,e,n,s = (0,-1),(0,1),(-1,0),(1,0)
previous = []
answers = []
rewards = []

################# Maze solver #################
# Path-0
# Wall-1
def maker(maze,pos,k):
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
            if(maze[north[0]][north[1]]==0 and north[0]>=0 and north[1]>=0):
                lis.append(north)
        except IndexError:
            pass

        try:
            if(maze[south[0]][south[1]]==0 and south[0]>=0 and south[1]>=0):
                lis.append(south)
        except IndexError:
            pass

        try:
            if(maze[west[0]][west[1]]==0 and west[0]>=0 and west[1]>=0):
                lis.append(west)
        except IndexError:
            pass

        try:
            if(maze[east[0]][east[1]]==0 and east[0]>=0 and east[1]>=0):
                lis.append(east)
        except IndexError:
            pass

        if(len(lis)==0):
            maze[pos[0]][pos[1]] = 2
            rewards[k][1] = rewards[k][1] - 5 
            rewards[k][2] = rewards[k][2] + 1
            try:
                pos = previous[-1]
                previous.pop()
            except IndexError:
                print("No way possible")
                return

        else:
            previous.append(pos)
            maze[pos[0]][pos[1]] = 9        
            pos = random.choice(lis)


# Main
mainmaze = [[0,0,1,1,0,0,0,1],
            [1,0,0,0,0,1,0,0],
            [0,0,1,1,1,1,1,0],
            [1,0,0,1,0,0,0,0],
            [1,1,0,1,0,1,0,0],
            [1,1,0,0,0,1,1,0],
            [1,1,1,1,0,0,1,0],
            [1,1,1,1,1,0,0,0]]
mainmaze.append("\n")


print("The original maze is \n")
for row in mainmaze:
    print(row)
mainmaze.pop()
t = []
u = int(input("Enter the no.of players:"))
for i in range(u):
    rewards.append([i,0,0,0])

# MultiThreading
for i in range(u):
    mazes = [[mainmaze[x][y] for y in range(len(mainmaze[0]))] for x in range(len(mainmaze))]
    t.append(threading.Thread(target=maker,args=(mazes,(0,0),i,)))
    t[-1].start()

for i in range(u):
    t[i].join()


# Answers
for i,answer in enumerate(answers):
    print("Player:",i+1)
    print()
    for row in answer:
        print(row)
    print()    
    print("Wrong Way :", rewards[i][2])
    print("Score :", rewards[i][1])
    print()

rewards = sorted(rewards,key=lambda x: x[1],reverse=True)
print(rewards)
print()
print("Winner is Player:",rewards[0][0]+1)