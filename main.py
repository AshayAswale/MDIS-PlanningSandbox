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


####### INIT VARIABLES #######
fig = plt.figure()
raw_floor_plan = np.loadtxt("building_floor_plan.txt", dtype=float)   # Copy of the floor plan
                                                                          # This copy will not be modified
scanned_floor_plan = deepcopy(raw_floor_plan)     # This copy will contain the boxes 
                                                      # that have been already scanned
meeting_location = np.array([8,5])    # Meeting Location
number_of_agents = 3      # Number of agents
list_of_agents = []     # List of agents' objects

# <Not sure exactly what these mean, but they are needed for animation>
im = plt.imshow(scanned_floor_plan)
im.set_array(scanned_floor_plan)


####### INIT CLASS OBJECTS #######
#
# Init agent objects
for i in range(number_of_agents):
  list_of_agents.append(Agent(meeting_location))

# Init Path Planner Object
path_planner = PathPlanner(scanned_floor_plan, np.array([8,5]), list_of_agents)


####### CALLBACK FOR ANIMATION #######
def updateMap(*args):

  # Plan the next steps for all the agents
  path_planner.planNextSteps()
  
  # This copy will be needed to display the agents' locations
  copy_of_scanned_plan = deepcopy(scanned_floor_plan)

  # Update Agents' current locations as 'Scanned Rooms' and Next locations as 'Agent Current Location'
  for agent in list_of_agents:
    copy_of_scanned_plan[agent.current_location[0], agent.current_location[1]] = SCANNED_ROOM_VALUE
    scanned_floor_plan[agent.current_location[0], agent.current_location[1]] = SCANNED_ROOM_VALUE

    copy_of_scanned_plan[agent.next_location[0], agent.next_location[1]] = AGENT_LOCATION_VALUE
    agent.updateAgentLocation()
  
  # Update animation grid with the current one
  im.set_array(copy_of_scanned_plan)
  return im,




####### ANIMATE THE GRAPH #######
ani = animation.FuncAnimation(fig, updateMap, interval=500, blit=True)
plt.show()
