import os
from rlvortex.envs.gym_wrapper.gym_envs import PendulumEnv
from rlvortex.utils import vlogger, trainer_utils
from rlvortex.trainer.ppo_trainer import NativePPOTrainer
from rlvortex.task_archive.ppo.hyperparams.gym_envs_params import (
    PendulumEnvParams,
)
from rlvortex.task_archive.ppo.hyperparams.gym_envs_params import global_seed
import random

if __name__ == "__main__":
    # trainer_utils.set_global_random_seed(rd_seed=seed)
    # env = PendulumEnv(render=False, seed=seed)
    ppo_trainer = NativePPOTrainer(
        env=PendulumEnvParams.env,
        policy=PendulumEnvParams.policy,
        optimizer=PendulumEnvParams.optimizer,
        init_lr=PendulumEnvParams.init_lr,
        device_id=-1,
        gamma=PendulumEnvParams.gamma,
        num_batches_per_env=PendulumEnvParams.num_batches_per_env,
        steps_per_env=PendulumEnvParams.steps_per_env,
        learning_iterations=PendulumEnvParams.learning_iterations,
        entropy_loss_coef=PendulumEnvParams.entropy_loss_coef,
        normalize_adv=False,
        random_sampler=PendulumEnvParams.random_sampler,
        enable_tensorboard=True,
        save_freq=50,
        log_type=vlogger.LogType.Screen,
        trainer_dir=os.path.join(os.getcwd(), "cache/ppo_trainers"),
        comment="pendulum",
    )
    ppo_trainer.train(PendulumEnvParams.epochs)
    avg_rtn, avg_len = ppo_trainer.evaluate(
        -1, env=PendulumEnv(viz=True)
    )
    print(f"avg_rtn: {avg_rtn}, avg_len: {avg_len}")