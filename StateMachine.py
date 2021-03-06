import numpy as np
from Agent import *
from PathPlanner import *

class StateMachine:
  def __init__(self, raw_floor_plan, number_of_agents, agent_entry_location, meeting_location, agent_exit_location, target_location, init_searching_timespan):
    self.raw_floor_plan = raw_floor_plan
    self.scanned_floor_plan = deepcopy(raw_floor_plan)
    self.list_of_agents = []
    self.meeting_location = meeting_location
    self.target_location = target_location
    self.searching_timespan = init_searching_timespan

    self.initClassObjects(number_of_agents, agent_entry_location, agent_exit_location)

  ### Function: Initialize Agent and Planner class objects
  #
  #
  def initClassObjects(self, number_of_agents, agent_entry_location,agent_exit_location):
    for i in range(number_of_agents):
      path=[]
      self.list_of_agents.append(Agent(agent_entry_location,agent_exit_location[i]))

    # Init Path Planner Object
    self.path_planner = PathPlanner(self.scanned_floor_plan, self.meeting_location, self.list_of_agents)
      

  ### Function: Plans the next state and returns the map to be animated
  #
  #

  def getNextState(self,iterate_path_count):
    if(iterate_path_count==0):
      self.path_planner.getNextMoves()
    # Plan next steps for all the agents

    self.path_planner.planNextSteps(iterate_path_count)
    iterate_path_count+=1

    # This copy will be needed to display the agents' locations
    copy_of_scanned_plan = deepcopy(self.scanned_floor_plan)

    # Update Agents' current locations as 'Scanned Rooms' and Next locations as 'Agent Current Location'
    for agent in self.list_of_agents:
      copy_of_scanned_plan[agent.current_location[0], agent.current_location[1]] = SCANNED_ROOM_VALUE
      self.scanned_floor_plan[agent.current_location[0], agent.current_location[1]] = SCANNED_ROOM_VALUE

      copy_of_scanned_plan[agent.next_location[0], agent.next_location[1]] = AGENT_LOCATION_VALUE
      agent.updateAgentLocation()
    
    return copy_of_scanned_plan

  