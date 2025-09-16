from tortoise import connections
from tortoise.transactions import in_transaction, atomic


async def raw_sql_dial_db_write():
    replica_conn = connections.get("replica")
    default_conn =connections.get("default")

    query = "INSERT INTO app_user(user_inn,email,password,user_name) VALUES($1, $2, $3, $4);"
    values = ['912344321', 'query_edit@postgres.io', 'postgre', 'query_edit']
    try:
        async with
    except Exception as e:
        del_default = default_conn.execute_query