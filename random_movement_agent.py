import numpy as np
import habitat
from habitat.sims.habitat_simulator.actions import HabitatSimActions


class RandomMovementAgent(habitat.Agent):

    def __init__(self, p_forward=0.3, p_left=0.3, p_right=0.3):
        self.p_forward = p_forward
        self.p_left = p_left
        self.p_right = p_right

    def act(self, observations):
        # if arrow keys pressed, give control to keyboard
        x = np.random.random()
        if x < self.p_forward:
            return HabitatSimActions.MOVE_FORWARD
        if x < self.p_forward + self.p_left:
            return HabitatSimActions.TURN_LEFT
        if x < self.p_forward + self.p_left + self.p_right:
            return HabitatSimActions.TURN_RIGHT
        return HabitatSimActions.STOP