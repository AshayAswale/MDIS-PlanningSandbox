import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PathPlanner import *
from StateMachine import *
from Agent import *
import numpy as np

### File Notations
### Unscanned Accessible Room - 1
### Scanned Accessible Room - 0.75
### Unaccessible Room / Wall - 0
### Agent Current Location - 0.25

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
resolution_multiplier = 3
raw_floor_plan = increaseResolution(raw_floor_plan, resolution_multiplier)
meeting_location = np.array([8,5])    # Meeting Location
agent_entry_location = meeting_location*resolution_multiplier + (int)(resolution_multiplier/2)   # Agents' Entry Location
number_of_agents = 3      # Number of agents
init_searching_timespan = 10    # First Meeting Time

# <Not sure exactly what these mean, but they are needed for animation>
im = plt.imshow(raw_floor_plan)
im.set_array(raw_floor_plan)

####### INIT CLASS OBJECTS #######
#
# Init State Machine
state_machine = StateMachine(raw_floor_plan, number_of_agents, agent_entry_location, meeting_location, init_searching_timespan)

####### CALLBACK FOR ANIMATION #######
def updateMap(*args):

  # Plan the next steps for all the agents
  current_floor_plan = state_machine.getNextState()
  
  # Update animation grid with the current one
  im.set_array(current_floor_plan)
  return im,




####### ANIMATE THE GRAPH #######
ani = animation.FuncAnimation(fig, updateMap, interval=500, blit=True)
plt.show()
