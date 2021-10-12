from copy import deepcopy
import numpy as np

class Agent:
  def __init__(self, starting_location) -> None:
    self.current_location = np.array(starting_location)
    self.distance_from_meeting_point = 0
    self.is_searching = True
    self.movement_history = []
    self.next_location = np.array(starting_location)

  def updateAgentLocation(self):
    self.current_location = deepcopy(self.next_location)