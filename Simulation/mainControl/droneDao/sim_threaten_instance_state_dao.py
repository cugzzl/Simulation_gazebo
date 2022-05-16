def get_sim_threaten_instance_state(db_pool, experiment_id, time):
    conn = db_pool.connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM sim_threaten_instance_state where sim_id='%d' and update_time='%d'" % (experiment_id, time)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result