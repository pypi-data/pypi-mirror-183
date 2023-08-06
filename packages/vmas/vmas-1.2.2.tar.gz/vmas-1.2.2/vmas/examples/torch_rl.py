#  Copyright (c) 2022-2023.
#  ProrokLab (https://www.proroklab.org/)
#  All rights reserved.
from torchrl.envs.libs.vmas import VmasEnv, VmasWrapper

import vmas

if __name__ == "__main__":
    # d = {
    #     "action": torch.randn(10, 32, 5, 100, 2, 6),
    #     "next": {"observation": torch.randn(10, 32, 5, 100, 18, 3)},
    # }
    # td1 = TensorDict(
    #     batch_size=(
    #         10,
    #         32,
    #         5,
    #         100,
    #     ),
    #     source=d,
    # )
    #
    # d2 = {
    #     "action": torch.randn(10, 32, 5, 100, 3, 9),
    #     "next": {"observation": torch.randn(10, 32, 5, 100, 8, 21)},
    # }
    # td2 = TensorDict(
    #     batch_size=(
    #         10,
    #         32,
    #         5,
    #         100,
    #     ),
    #     source=d2,
    # )
    #
    # het_td: LazyStackedTensorDict = torch.stack([td1, td2])
    # print(het_td)

    arguments = {
        "scenario_name": "flocking",
        "num_envs": 3,
        "continuous_actions": True,
        "n_agents": 2,
    }

    env = VmasEnv(**arguments)
    wrapped = VmasWrapper(env=vmas.make_env(**arguments))

    env.set_seed(1)
    wrapped.set_seed(1)

    print(env.observation_spec)

    # for dirpath, dirnames, filenames in os.walk(
    #     osp.dirname(
    #         "/Users/Matteo/PycharmProjects/VectorizedMultiAgentSimulator/vmas/scenarios/"
    #     )
    # ):
    #     for filename in filenames:
    #         if filename == ".DS_Store" or filename == "__init__.py":
    #             continue
    #         print(f"Testing: {filename}")
    #         try:
    #             env = vmas.make_env(
    #                 scenario_name=filename,
    #                 num_envs=32,
    #                 device="cpu",
    #                 continuous_actions=False,
    #                 max_steps=100,
    #                 wrapper=vmas.Wrapper.TORCHRL,
    #                 # n_agents=4,
    #             )
    #             env.rand_step()
    #         except:
    #             print("FAILED")
