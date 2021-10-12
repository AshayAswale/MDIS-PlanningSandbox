from copy import deepcopy
import numpy as np

UNSCANNED_ROOM_VALUE = 1
SCANNED_ROOM_VALUE = 0.75
UNACCESSIBLE_ROOM_VALUE = 0
AGENT_LOCATION_VALUE = 0.25

class Agent:
  def __init__(self, starting_location) -> None:
    self.current_location = np.array(starting_location) # Current Location in the grid
    self.distance_from_meeting_point = 0                # How long will it take to get to meeting point
    self.is_searching = True                            # New location when search True, 
                                                            # Plan to meeting point when False
    self.movement_history = []                          # History of locations that agent has been to
    self.next_location = np.array(starting_location)    # Next Location planned for the agent

### @Function: Updates the Agent Location from next to current
#
  def updateAgentLocation(self):
    self.current_location = deepcopy(self.next_location)