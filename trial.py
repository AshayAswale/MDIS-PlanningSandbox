import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from copy import deepcopy
import random 
import math

fig = plt.figure()
first = True
T = 0
size = 100

meeting_point = [(int)(size/2), (int)(size/2)]
agent_1 = [meeting_point[0]-1, meeting_point[1]]
agent_2 = [meeting_point[0], meeting_point[1]-1]
agent_3 = [meeting_point[0], meeting_point[1]+1]

meeting_time = 10
last_meeting_time = 0
suveil_map = np.zeros([size,size])
movement_agent_1 = 0

search_agent_1 = True
reached_home_1 = False

def getFireflies():
  # global first
  suveil_map[agent_1[0], agent_1[1]]=0.5
  suveil_map[agent_2[0], agent_2[1]]=0.5
  suveil_map[agent_3[0], agent_3[1]]=0.5

  fireflies = deepcopy(suveil_map)
  
  # if first:
  #   fireflies[0,0] = 1.0
  #   first = False
  ###

  fireflies[agent_1[0], agent_1[1]]=1
  fireflies[agent_2[0], agent_2[1]]=1
  fireflies[agent_3[0], agent_3[1]]=1
  return fireflies

def getAgent(n):
  if n==1:
    return agent_1
  elif n == 2:
    return agent_2
  else:
    return agent_3

def moveAgent(agent, n, time_remain, search):
  dist = abs(agent[0]-meeting_point[0]) + abs(agent[1] - meeting_point[1])
  # print(time_remain)
  # if dist<time_remain:
  # print(time_remain)
  if dist<time_remain and search:
    # print(time_remain)
    x = 0 if time_remain%2==0 else 1 if not n == 1 else -1
    y = 1 if n == 3 else -1 if x==0 else 0
    # print("out")
    return [min(agent[0]+x, size), min((agent[1]+y), size)], search
  else:
    x = 0 if time_remain%2==0 else math.copysign(0 if meeting_point[0]-agent[0] == 0 else 1, meeting_point[0]-agent[0])
    y = 0 if abs(x)==1 else math.copysign(0 if meeting_point[1]+1-agent[1] == 0 else 1, meeting_point[1]+1-agent[1])
    # print("in")
    # print(x, y)
    # print((x==0 and y==0))
    return [agent[0]+(int)(x), agent[1]+(int)(y)], (x==0 and y==0)
    # return agent_1



def updateBoard(size):
  global agent_1, agent_2, agent_3
  global T, movement_agent_1, search_agent_1, meeting_time, last_meeting_time
  x = T%4
  # if(x==0):
  #   agent_1 = [agent_1[0], agent_1[1] + 5]
  # elif(x==1):
  #   agent_1 = [agent_1[0] - 5, agent_1[1]]
  # elif(x==2):
  #   agent_1 = [agent_1[0] + 5, agent_1[1]]
  # else:
  #   agent_1 = [agent_1[0], agent_1[1] - 5]
  time_remaining =meeting_time- (T-last_meeting_time)%meeting_time
  # print(time_remaining)
  prev_search = search_agent_1
  agent_3, search_agent_1 = moveAgent(agent_3, 3, time_remaining, search_agent_1)
  agent_2, search_agent_2 = moveAgent(agent_2, 2, time_remaining, search_agent_1)
  agent_1, search_agent_3 = moveAgent(agent_1, 1, time_remaining, search_agent_1)
  if not prev_search and search_agent_1:
    meeting_time += 10
    last_meeting_time = T
    # print(T, meeting_time, last_meeting_time)
  T+=1
  return getFireflies()


im = plt.imshow(updateBoard(size), animated=True)

def updatefig(*args):
  im.set_array(updateBoard(size))
  return im,

ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
plt.show()