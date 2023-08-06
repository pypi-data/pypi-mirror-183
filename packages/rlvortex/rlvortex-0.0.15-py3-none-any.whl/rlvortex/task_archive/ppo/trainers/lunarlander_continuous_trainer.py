import os
from vortex.envs.gym_wrapper.gym_envs import LunarLanderEnv
from vortex.trainer.ppo_trainer import NativePPOTrainer
from vortex.utils import vlogger
from vortex.task_archive.ppo.hyperparams.gym_envs_params import LunarLanderContinuousEnvParams as env_params

if __name__ == "__main__":
    ppo_trainer = NativePPOTrainer(
        env=env_params.env,
        policy=env_params.policy,
        optimizer=env_params.optimizer,
        steps_per_env=env_params.steps_per_env,
        num_batches_per_env=env_params.num_batches_per_env,
        learning_iterations=env_params.learning_iterations,
        val_loss_coef=env_params.val_loss_coef,
        init_lr=env_params.actor_lr,
        random_sampler=env_params.random_sampler,
        normalize_adv=env_params.normalize_adv,
        enable_tensorboard=True,
        save_freq=10,
        log_type=vlogger.LogType.Screen,
        trainer_dir=os.path.join(os.getcwd(), "cache/ppo_trainers"),
        comment="lunarlander-continuous",
    )
    train_batch = 5
    sub_steps = int(env_params.epochs // train_batch)
    ppo_trainer.evaluate(5, env=LunarLanderEnv(render=True))
    for _ in range(train_batch):
        ppo_trainer.train(sub_steps)
        input("Press any key to evaluate and continue training...")
        ep_rtn,ep_mean = ppo_trainer.evaluate(1, env=LunarLanderEnv(render=True))
        print("ep_rtn:",ep_rtn,"ep_mean:",ep_mean)
    ppo_trainer.evaluate(-10, env=LunarLanderEnv(render=True))
