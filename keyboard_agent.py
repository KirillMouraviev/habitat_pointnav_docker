import habitat
from habitat.sims.habitat_simulator.actions import HabitatSimActions
import keyboard

class KeyboardAgent(habitat.Agent):
    def __init__(self):
        self.speed = 0.
        self.twist = 1.

    def reset(self):
        pass

    def get_actions_from_keyboard(self):
        if keyboard.is_pressed('left'):
            return HabitatSimActions.TURN_LEFT
        elif keyboard.is_pressed('right'):
            return HabitatSimActions.TURN_RIGHT
        elif keyboard.is_pressed('up'):
            return HabitatSimActions.MOVE_FORWARD
        elif keyboard.is_pressed('s'):
            return HabitatSimActions.STOP
        return None

    def act(self, observations):
        # receive command from keyboard and move
        print('Waiting action from keyboard: arrows to move, "S" to stop')
        action = self.get_actions_from_keyboard()
        while action is None:
            action = self.get_actions_from_keyboard()
        print('Done!')
        return action