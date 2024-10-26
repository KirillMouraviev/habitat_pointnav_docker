#! /usr/bin/env python

import numpy as np
np.float = np.float64

import habitat
from habitat.sims.habitat_simulator.actions import HabitatSimActions
from keyboard_agent import KeyboardAgent
from random_movement_agent import RandomMovementAgent
# from custom_sensors import AgentPositionSensor
from habitat_map.mapper import Mapper
from habitat_baselines.config.default import get_config
import os

class HabitatRunner():
    def __init__(self):
        # Initialize ROS node and take arguments
        task_config = '/root/configs/pointnav_gibson.yaml'
        print('TASK CONFIG:', task_config)

        # Now define the config for the sensor
        habitat_path = '/data'
        config = habitat.get_config(task_config)
        config.defrost()
        #config.DATASET.DATA_PATH = os.path.join(habitat_path, 'datasets/objectnav_hm3d_v1/val/val.json.gz')
        #config.DATASET.CONTENT_SCENES = ['mv2HUxq3B53']
        config.ENVIRONMENT.ITERATOR_OPTIONS.SHUFFLE = False
        print(config.DATASET)
        config.SIMULATOR.SCENE_DATASET = os.path.join(habitat_path, "scene_datasets/hm3d/hm3d_annotated_basis.scene_dataset_config.json")
        #config.SIMULATOR.SCENE = 'mv2HUxq3B53'
        print('PATH:', config.SIMULATOR.SCENE_DATASET)
        config.TASK.MEASUREMENTS.append("TOP_DOWN_MAP")
        config.TASK.SENSORS.append("HEADING_SENSOR")
        config.freeze()
        self.config = config

        # Initialize the agent and environment
        self.env = habitat.Env(config=config)
        # self.eval_episodes = self.env.scenes_eps
        print('Environment created')

        agent_type = 'keyboard'
        if agent_type == 'keyboard':
           self.agent = KeyboardAgent()
        elif agent_type == 'random_movement':
            self.agent = RandomMovementAgent()
        else:
            print('AGENT TYPE {} IS NOT DEFINED!!!'.format(agent_type))
            return

    def run_episode(self):
        observations = self.env.reset()
        self.agent.reset()
        step = 0
        while not self.env.episode_over:
            action = self.agent.act(observations)
            observations = self.env.step(action)
            step += 1
        metrics = self.env.task.measurements.get_metrics()
        print('METRICS:', metrics)
        success = metrics['success']
        spl = metrics['spl']
        return success, spl

def main():
    runner = HabitatRunner()
    successes = []
    spls = []
    for ep in runner.env._episodes:
        success, spl = runner.run_episode()
        successes.append(success)
        spls.append(spl)
    print('Success rate:', np.mean(successes))
    print('Average SPL:', np.mean(spls))

if __name__ == '__main__':
    main()
