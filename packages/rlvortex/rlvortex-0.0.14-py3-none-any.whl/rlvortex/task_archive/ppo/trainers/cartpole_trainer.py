import os
from rlvortex.envs.gym_wrapper.gym_envs import CartPoleEnv
from rlvortex.trainer.ppo_trainer import NativePPOTrainer
from rlvortex.utils import vlogger
from rlvortex.task_archive.ppo.hyperparams.gym_envs_params import CartpoleEnvParams as env_params
if __name__ == "__main__":
    ppo_trainer = NativePPOTrainer(
        env= env_params.env,
        policy=env_params.policy,
        optimizer=env_params.optimizer,
        init_lr=env_params.init_lr,
        enable_tensorboard=True,
        device_id=-1,
        save_freq=5,
        log_type=vlogger.LogType.Screen,
        trainer_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache/ppo_trainers"),
        comment="cartpole"
    )
    train_batch = 5
    sub_steps = int(env_params.epochs // train_batch)
    ppo_trainer.evaluate(1, env=CartPoleEnv(viz=False))
    for _ in range(train_batch):
        ppo_trainer.train(sub_steps)
        ep_rtn,ep_mean = ppo_trainer.evaluate(1, env=CartPoleEnv(viz=False))
        print("ep_rtn:",ep_rtn,"ep_mean:",ep_mean)
    ppo_trainer.evaluate(-1, env=CartPoleEnv(viz=False))
   