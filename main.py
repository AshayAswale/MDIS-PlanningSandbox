import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PathPlanner import *
from Agent import *
import numpy as np

### File Notations
### Unscanned Accessible Room - 1
### Scanned Accessible Room - 0.75
### Unaccessible Room / Wall - 0
### Agent Current Location - 0.25

UNSCANNED_ROOM_VALUE = 1
SCANNED_ROOM_VALUE = 0.75
UNACCESSIBLE_ROOM_VALUE = 0
AGENT_LOCATION_VALUE = 0.25


####### INIT VARIABLES #######
fig = plt.figure()
raw_floor_plan = np.loadtxt("building_floor_plan.txt", dtype=float)
scanned_floor_plan = deepcopy(raw_floor_plan)
meeting_location = np.array([8,5])
number_of_agents = 1
list_of_agents = []
im = plt.imshow(scanned_floor_plan)
im.set_array(scanned_floor_plan)


####### INIT CLASS OBJECTS #######
for i in range(number_of_agents):
  list_of_agents.append(Agent(meeting_location))
path_planner = PathPlanner(scanned_floor_plan, np.array([8,5]), list_of_agents)


####### ANIMATE THE GRAPH #######
p = 5
def updateMap(*args):

  ####### UPDATE THE GRAPHS #######
  path_planner.planNextSteps()
  
  copy_of_scanned_plan = deepcopy(scanned_floor_plan)
  for agent in list_of_agents:
    copy_of_scanned_plan[agent.current_location[0], agent.current_location[1]] = SCANNED_ROOM_VALUE
    scanned_floor_plan[agent.current_location[0], agent.current_location[1]] = SCANNED_ROOM_VALUE

    copy_of_scanned_plan[agent.next_location[0], agent.next_location[1]] = AGENT_LOCATION_VALUE
    agent.updateAgentLocation()
  
  im.set_array(copy_of_scanned_plan)
  return im,




####### ANIMATE THE GRAPH #######
ani = animation.FuncAnimation(fig, updateMap, interval=500, blit=True)
plt.show()
