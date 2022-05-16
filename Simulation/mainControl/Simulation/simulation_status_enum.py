from enum import Enum


# 事件类型
class Event(Enum):
    UAV_ACTION = 0
    BOOM = 1
    ORIGINAL_TARGET = 2


# 无人机状态
class Uav_Status(Enum):
    FLAYING = 1
    SCOUT = 2
    ATTACK = 3
    HOVER = 4


# 突发状况类型
class Sudden(Enum):
    TARGET = 1
    UAV = 0
    THREATEN = 2


#    打击目标是否被侦察到
class Is_Detected(Enum):
    YES = 1
    No = 0


class Task_Type(Enum):
    SCOUT = 1
    ATTACK = 2