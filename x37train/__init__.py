# Copyright (c) 2022-2025, Custom Robot Project
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""X37 robot task registration."""

import gymnasium as gym

##
# Register Gym environments.
##

gym.register(
    id="X37-Velocity",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.velocity_env_cfg:RobotEnvCfg",
        "play_env_cfg_entry_point": f"{__name__}.velocity_env_cfg:RobotPlayEnvCfg",
        "rsl_rl_cfg_entry_point": f"unitree_rl_lab.tasks.locomotion.agents.rsl_rl_ppo_cfg:BasePPORunnerCfg",
    },
)
