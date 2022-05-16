# -*- coding=utf-8 -*-

from mainControl.Simulation.start_simulation_process import start_simulation



if __name__ == '__main__':
    # 从唐总获得试验id
    # experiment_id = sys.argv[0]
    experiment_id = 100
    start_simulation(experiment_id)

