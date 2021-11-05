import numpy as np
from copy import deepcopy
from Agent import *
from search import astar
import random

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
  

  ### Function: Checks for the boundary, 
  # True: Chosen move can be made
  # False: Chosen move out of grid
  #


  # def checkBoundary(self, grid_size, i, j):
  #   if (i<0 or j<0):
  #     return False
    
  #   if (i>(grid_size[0]-1) or j>(grid_size[1]-1)):
  #     return False

  #   return True


  ### Function: Retruns a randomly chosen possible move
  # @param: agent_location    [1x2] list    Agent's current location
  # @param: is_searching      bool          is the agent searching or going to meeting point
  #

  def getNextMoves(self):
    for agent in self.list_of_agents:
      astar_path, aster_steps = astar(self.grid, agent.current_location, agent.final_location)
      agent.path=astar_path

  def getPossibleNeighbour(self, agent_location, is_searching):
    list_of_possible_moves = []
    x = agent_location[0] # I know this is actually inverted,
    y = agent_location[1] # but it makes more sense while reading
    
    locs = [[x-1,y],[x+1,y],[x,y+1],[x,y-1]]
    for loc in locs:
      if(self.checkBoundary(self.grid.shape, loc[0],loc[1])):
        if (self.grid[loc[0],loc[1]] == UNSCANNED_ROOM_VALUE):
          list_of_possible_moves.append(loc)
    return random.choice(list_of_possible_moves) if len(list_of_possible_moves)>0 else agent_location


  ## Function: Plans the next steps for all the agents
  
  def planNextSteps(self,iter_count):
    # print(iter_count)
    for agent in self.list_of_agents:
      # agent.next_location = self.getPossibleNeighbour(agent.current_location, True)
      if(iter_count<len(agent.path)):
        agent.next_location = agent.path[iter_count]
      else:
        agent.next_location = agent.path[-1]