
仿真过程中无人机指令相关数据格式（代码层面）：
	
	uav_static_param --无人机静态参数数据格式
		{uav_id: [uav_id, uav_type_category, uav_type_id, action_interval_time, radius]}
	
	uav_speed -- 无人机飞行速度数据格式
		{uav_id: uav_speed}
	
	uav_load -- 无人机当前载弹量数据格式
		{uav_id: uav_load}
		
	uav_max_distance -- 无人机当前载弹量数据格式
		{uav_id: max_distance}
		
	uav_distance --无人机当前飞行距离数据格式
		{uav_id: distance}

	gazebo_uav_status --无人机真实数据返回指令格式：
		[[uav_id, uav_real_position, uav_orientation, uav_action_status, uav_next_point, action_keep_time]]
		
	shared_current_uav_status --仿真中需要保存至数据库的实时状态数据格式：
		[[uav_id, str(uav_real_position), str(uav_orientation), 
			uav_name, uav_type_id, experiment_id, current_step, uav_current_load, current_max_distance,
				current_map_x, current_map_y, current_map_z, Q_x, Q_Y, Q_z, Q_w]]
				
	pre_step_uav_status和current_all_uav_status --重规划时需要用到的无人机当前态势数据格式：
		[[uav_id, uav_real_position, uav_orientation, uav_action_status, uav_next_point, action_keep_time, 
			uav_name, uav_type_id, experiment_id, current_step, uav_current_load, current_max_distance]]