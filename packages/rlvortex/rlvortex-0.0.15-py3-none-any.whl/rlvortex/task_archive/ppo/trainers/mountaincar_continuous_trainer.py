import os
from vortex.envs.gym_wrapper.gym_envs import MountainCarContinuousEnv
from vortex.utils import vlogger, trainer_utils
from vortex.trainer.ppo_trainer import NativePPOTrainer
from vortex.task_archive.ppo.hyperparams.gym_envs_params import MountainCarContinuousEnvParams as env_params

if __name__ == "__main__":
    # seed = 314
    # trainer_utils.set_global_random_seed(rd_seed=seed)
    # env = MountainCarContinuousEnv(render=False, seed=seed)
    ppo_trainer = NativePPOTrainer(
        env=env_params.env,
        policy=env_params.policy,
        optimizer=env_params.optimizer,
        init_lr=env_params.init_lr,
        val_loss_coef=env_params.val_loss_coef,
        num_batches_per_env=env_params.num_batches_per_env,
        steps_per_env=env_params.steps_per_env,
        learning_iterations=env_params.learning_iterations,
        entropy_loss_coef=env_params.entropy_loss_coef,
        max_grad_norm=env_params.max_grad_norm,
        normalize_adv=env_params.normalize_adv,
        enable_tensorboard=True,
        save_freq=50,
        log_type=vlogger.LogType.Screen,
        trainer_dir=os.path.join(os.getcwd(), "cache/ppo_trainers"),
        comment="mountaincar-continuous",
    )

    train_batch = 3
    sub_steps = int(env_params.epochs // train_batch)
    ppo_trainer.evaluate(1, env=MountainCarContinuousEnv(render=True))
    for _ in range(train_batch):
        ppo_trainer.train(sub_steps)
        input("Press any key to evaluate and continue training...")
        ep_rtn,ep_mean = ppo_trainer.evaluate(1, env=MountainCarContinuousEnv(render=True))
        print("ep_rtn:",ep_rtn,"ep_mean:",ep_mean)
    ppo_trainer.evaluate(-1, env=MountainCarContinuousEnv(render=True))
   
