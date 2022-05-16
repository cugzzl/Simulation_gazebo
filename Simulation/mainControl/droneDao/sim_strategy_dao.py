def get_algo_param_id_scenario(db_pool, strategy_id):
    conn = db_pool.connection()
    cursor = conn.cursor()

    sql = 'select algo_param_id1, algo_param_id3 from sim_strategy where strategy_id=%d' % strategy_id
    cursor.execute(sql)

    result = cursor.fetchall()

    return result