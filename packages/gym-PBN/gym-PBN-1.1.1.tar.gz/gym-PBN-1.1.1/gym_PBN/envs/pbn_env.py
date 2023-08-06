from typing import List, Set, Tuple, Union
import random

import gymnasium as gym
import networkx as nx
import numpy as np
from gymnasium.spaces import Discrete, MultiBinary
from gym_PBN.types import GYM_STEP_RETURN, REWARD, STATE, TERMINATED, TRUNCATED

from .common.pbn import PBN


class PBNEnv(gym.Env):
    metadata = {"render_modes": ["human", "PBN", "STG", "funcs", "idx", "float"]}

    def __init__(
        self,
        render_mode: str = "human",
        render_no_cache: bool = False,
        PBN_data=[],
        logic_func_data=None,
        name: str = None,
        goal_config: dict = None,
        reward_config: dict = None,
    ):
        self.PBN = PBN(PBN_data, logic_func_data)

        # Goal configuration
        goal_config = self._check_config(
            goal_config, "goal", set(["target", "all_attractors"])
        )
        if (
            goal_config is None
        ):  # If no goal config is provided, then compute attractors and set the target as the last attractor.
            goal_config = {}
            goal_config["all_attractors"] = self.compute_attractors()
            goal_config["target"] = goal_config["all_attractors"][-1]
        else:
            assert (
                type(goal_config["target"]) is set
            ), "Did you put multiple attractors as the target by mistake?"
        self.target = goal_config["target"]
        self.all_attractors = goal_config["all_attractors"]

        # Reward configuration
        reward_config = self._check_config(
            reward_config,
            "reward",
            set(["successful_reward", "wrong_attractor_cost", "action_cost"]),
            default_values={
                "successful_reward": 10,
                "wrong_attractor_cost": 2,
                "action_cost": 1,
            },
        )
        self.successful_reward = reward_config["successful_reward"]
        self.wrong_attractor_cost = reward_config["wrong_attractor_cost"]
        self.action_cost = reward_config["action_cost"]

        # Gym
        self.observation_space = MultiBinary(self.PBN.N)
        self.observation_space.dtype = bool
        self.action_space = Discrete(self.PBN.N + 1)
        self.name = name
        self.render_mode = render_mode
        self.render_no_cache = render_no_cache

    def _seed(self, seed: int = None):
        np.random.seed(seed)
        random.seed(seed)

    def _check_config(
        self,
        config: dict,
        _type: str,
        required_keys: Set[str],
        default_values: dict = None,
    ) -> dict:
        """Small utility function to validate an environment config.

        Args:
            config (dict): The config to validate.
            _type (str): The type of config this is about. Just needs to be a semantically rich string for the exception output.
            required_keys (Set[str]): The mandatory keys that need to be in the config.
            default_values (dict, optional): The default values for the config should it be empty. Defaults to None.

        Raises:
            ValueError: Thrown when some or all of the required keys are missing in the given config values.

        Returns:
            dict: The config after it has been checked and initialized to default values if it was empty to begin with.
        """
        if config:
            missing_keys = required_keys - set(config.keys())
            if len(missing_keys) > 1:  # If any of the required keys are missing
                raise ValueError(
                    f"Invalid {_type} config provided. The following required values are missing: {', '.join(missing_keys)}."
                )
        else:
            config = default_values

        return config

    def step(self, action: int = 0) -> GYM_STEP_RETURN:
        """Transition the environment by 1 step. Optionally perform an action.

        Args:
            action (int, optional): The action to perform (1-indexed node to flip). Defaults to 0, meaning no action.

        Raises:
            Exception: When the action is outside the action space.

        Returns:
            GYM_STEP_RETURN: The typical Gymnasium environment 5-item Tuple.\
                 Consists of the resulting environment state, the associated reward, the termination / truncation status and additional info.
        """
        if not self.action_space.contains(action):
            raise Exception(f"Invalid action {action}, not in action space.")

        if action != 0:  # Action 0 is taking no action.
            self.PBN.flip(action - 1)

        self.PBN.step()

        observation = self.PBN.state
        reward, terminated, truncated = self._get_reward(observation, action)
        info = {"observation_idx": self._state_to_idx(observation)}

        return observation, reward, terminated, truncated, info

    def _get_reward(
        self, observation: STATE, action: int
    ) -> Tuple[REWARD, TERMINATED, TRUNCATED]:
        """The Reward function.

        Args:
            observation (STATE): The next state observed as part of the action.
            action (int): The action taken.

        Returns:
            Tuple[REWARD, TERMINATED, TRUNCATED]: Tuple of the reward and the environment done status.
        """
        reward, terminated, truncated = 0, False, False
        observation_tuple = tuple(observation)

        if observation_tuple in self.target:
            reward += self.successful_reward
            terminated = True
        else:
            attractors_matched = sum(
                observation_tuple in attractor for attractor in self.all_attractors
            )
            reward -= self.wrong_attractor_cost * attractors_matched

        if action != 0:
            reward -= self.action_cost

        return reward, terminated, truncated

    def reset(self, seed: int = None, options: dict = None) -> tuple[STATE, dict]:
        """Reset the environment. Initialise it to a random state."""
        if seed is not None:
            self._seed(seed)

        state = None
        if options is not None and "state" in options:
            state = self.PBN.reset(options["state"])
        observation = self.PBN.reset(state)
        info = {"observation_idx": self._state_to_idx(observation)}
        return observation, info

    def render(self):
        mode = self.render_mode
        no_cache = self.render_no_cache

        if mode == "human":
            return self.PBN.state
        elif mode == "PBN":
            return self.PBN.print_PBN(no_cache)
        elif mode == "STG":
            return self.PBN.print_STG(no_cache)
        elif mode == "funcs":
            return self.PBN.print_functions()
        elif mode == "idx":
            return self._state_to_idx(self.PBN.state)
        elif mode == "float":
            return [float(x) for x in self.PBN.state]

    def _state_to_idx(self, state: STATE):
        return int(
            "".join([str(x) for x in np.array(state, dtype=np.int8).tolist()]), 2
        )

    def compute_attractors(self):
        print("Computing attractors...")
        STG = self.render(mode="STG")
        generator = nx.algorithms.components.attracting_components(STG)
        return self._nx_attractors_to_tuples(list(generator))

    def _nx_attractors_to_tuples(self, attractors):
        return [
            set(
                [
                    tuple([int(x) for x in state.lstrip("[").rstrip("]").split()])
                    for state in list(attractor)
                ]
            )
            for attractor in attractors
        ]

    def clip(self, gene_i):
        self.PBN.clip(gene_i)

    def close(self):
        """Close out the environment and make sure everything is garbage collected."""
        del self.PBN
