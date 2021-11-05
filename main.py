import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PathPlanner import *
from StateMachine import *
from Agent import *
import numpy as np
import time
from matplotlib.patches import Rectangle
from search import astar

### File Notations
### Unscanned Accessible Room - 1
### Scanned Accessible Room - 0.75
### Unaccessible Room / Wall - 0
### Agent Current Location - 0.25

# def draw_path(grid, start, goal, path, title):
#     # Visualization of the found path using matplotlib
#     fig, ax = plt.subplots(1)
#     ax.margins()
#     # Draw map
#     row = len(grid)     # map size
#     col = len(grid[0])  # map size
#     for i in range(row):
#         for j in range(col):
#             if grid[i][j]: 
#                 ax.add_patch(Rectangle((j-0.5, i-0.5),1,1,edgecolor='k',facecolor='w'))  # obstacle
#             else:          
#                 ax.add_patch(Rectangle((j-0.5, i-0.5),1,1,edgecolor='k',facecolor='k'))  # free space
#     # Draw path
#     for x, y in path:
#         ax.add_patch(Rectangle((y-0.5, x-0.5),1,1,edgecolor='k',facecolor='b'))          # path
#     ax.add_patch(Rectangle((start[1]-0.5, start[0]-0.5),1,1,edgecolor='k',facecolor='g'))# start
#     ax.add_patch(Rectangle((goal[1]-0.5, goal[0]-0.5),1,1,edgecolor='k',facecolor='r'))  # goal
#     # Graph settings
#     plt.title(title)
#     plt.axis('scaled')
#     plt.gca().invert_yaxis()

def increaseResolution(input_floor_plan, resolution_multiplier):
  new_floor_plan = np.zeros([(int)(input_floor_plan.shape[0]*resolution_multiplier), (int)(input_floor_plan.shape[1]*resolution_multiplier)], dtype=float)
  for i, col in enumerate(input_floor_plan):
    for j, row in enumerate(col):
      new_floor_plan[i*resolution_multiplier:(i+1)*resolution_multiplier, j*resolution_multiplier:(j+1)*resolution_multiplier] = input_floor_plan[i,j]
  return new_floor_plan

####### INIT VARIABLES #######
fig = plt.figure()
raw_floor_plan = np.loadtxt("building_floor_plan.txt", dtype=float)   # Copy of the floor plan
                                                                          # This copy will not be modified
resolution_multiplier = 4

meeting_location = np.array([8,5])    # Meeting Location
target_location = []  #Target Location for Path Planner
number_of_agents = 5     # Number of agents
init_searching_timespan = 10    # First Meeting Time

for i in range(number_of_agents):
    found=False
    while(found==False):
      sample=[np.random.randint(0,len(raw_floor_plan)),np.random.randint(0,len(raw_floor_plan[0]))]
      if raw_floor_plan[sample[0]][sample[1]]==1:
        target_location.append(np.array(sample))
        found=True

raw_floor_plan = increaseResolution(raw_floor_plan, resolution_multiplier)
agent_entry_location = meeting_location*resolution_multiplier + (int)(resolution_multiplier/2)   # Agents' Entry Location
agent_exit_location = []
for j in range(number_of_agents):
  agent_exit_location.append(target_location[j]*resolution_multiplier + (int)(resolution_multiplier/2))

# <Not sure exactly what these mean, but they are needed for animation>
im = plt.imshow(raw_floor_plan)
im.set_array(raw_floor_plan)

####### INIT CLASS OBJECTS #######
#
# Init State Machine

state_machine = StateMachine(raw_floor_plan, number_of_agents, agent_entry_location, meeting_location, agent_exit_location, target_location, init_searching_timespan)
####### CALLBACK FOR ANIMATION #######
# state_machine.getNextState()
iterate_path_count=0
def updateMap(*args):
  global iterate_path_count
#   # Plan the next steps for all the agents
  current_floor_plan = state_machine.getNextState(iterate_path_count)
  iterate_path_count+=1
#   # Update animation grid with the current one
  im.set_array(current_floor_plan)
  return im,


# ####### ANIMATE THE GRAPH #######
ani = animation.FuncAnimation(fig, updateMap, interval=500, blit=True)
plt.show()

