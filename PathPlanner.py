import numpy as np
from copy import deepcopy
import math

### @package: PathPlanner
# 
# Standalone module for path planner.
#
#
class PathPlanner:
  
  ### Function: init function for path planner
  # @param grid_size:         [1x2] array: Grid size
  # @param meeting_point:     [1x2] array: Coordinates for the meeting_point.
  # @param number_of_agents:  list       : list of agents
  #
  def __init__(self, grid, meeting_point, list_of_agents) -> None:
    self.grid = grid
    self.meeting_point = meeting_point
    self.list_of_agents = list_of_agents
  

  ### Function: Plans the next steps for all the agents
  #
  def planNextSteps(self):
    for agent in self.list_of_agents:
      x = agent.next_location[1]+1
      y = agent.next_location[0]
      agent.next_location = [y,x]
      