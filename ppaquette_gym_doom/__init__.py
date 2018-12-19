from gym.envs.registration import register
from .package_info import USERNAME
from .doom_env import DoomEnv, MetaDoomEnv
from .doom_basic import DoomBasicEnv
from .doom_corridor import DoomCorridorEnv
from .doom_defend_center import DoomDefendCenterEnv
from .doom_defend_line import DoomDefendLineEnv
from .doom_health_gathering import DoomHealthGatheringEnv
from .doom_my_way_home import DoomMyWayHomeEnv
from .doom_predict_position import DoomPredictPositionEnv
from .doom_take_cover import DoomTakeCoverEnv
from .doom_deathmatch import DoomDeathmatchEnv

# Env registration
# ==========================

register(
    id='{}/meta-Doom-v0'.format(USERNAME),
    entry_point='{}_gym_doom:MetaDoomEnv'.format(USERNAME),
    max_episode_steps=999999,
    reward_threshold=9000.0,
    kwargs={
        'average_over': 3,
        'passing_grade': 600,
        'min_tries_for_avg': 3
    },
)

register(
    id='{}/DoomBasic-v0'.format(USERNAME),
    entry_point='{}_gym_doom:DoomBasicEnv'.format(USERNAME),
    max_episode_steps=10000,
    reward_threshold=10.0,
)

register(
    id='{}/DoomCorridor-v0'.format(USERNAME),
    entry_point='{}_gym_doom:DoomCorridorEnv'.format(USERNAME),
    max_episode_steps=10000,
    reward_threshold=1000.0,
)

register(
    id='{}/DoomDefendCenter-v0'.format(USERNAME),
    entry_point='{}_gym_doom:DoomDefendCenterEnv'.format(USERNAME),
    max_episode_steps=10000,
    reward_threshold=10.0,
)

register(
    id='{}/DoomDefendLine-v0'.format(USERNAME),
    entry_point='{}_gym_doom:DoomDefendLineEnv'.format(USERNAME),
    max_episode_steps=10000,
    reward_threshold=15.0,
)

register(
    id='{}/DoomHealthGathering-v0'.format(USERNAME),
    entry_point='{}_gym_doom:DoomHealthGatheringEnv'.format(USERNAME),
    max_episode_steps=10000,
    reward_threshold=1000.0,
)

register(
    id='{}/DoomMyWayHome-v0'.format(USERNAME),
    entry_point='{}_gym_doom:DoomMyWayHomeEnv'.format(USERNAME),
    max_episode_steps=10000,
    reward_threshold=0.5,
)

register(
    id='{}/DoomPredictPosition-v0'.format(USERNAME),
    entry_point='{}_gym_doom:DoomPredictPositionEnv'.format(USERNAME),
    max_episode_steps=10000,
    reward_threshold=0.5,
)

register(
    id='{}/DoomTakeCover-v0'.format(USERNAME),
    entry_point='{}_gym_doom:DoomTakeCoverEnv'.format(USERNAME),
    max_episode_steps=10000,
    reward_threshold=750.0,
)

register(
    id='{}/DoomDeathmatch-v0'.format(USERNAME),
    entry_point='{}_gym_doom:DoomDeathmatchEnv'.format(USERNAME),
    max_episode_steps=10000,
    reward_threshold=20.0,
)
