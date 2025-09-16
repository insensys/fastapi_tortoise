from tortoise import connections, run_async
from tortoise import Tortoise


DB_URL="asyncpg://localhost_user:1234@localhost:5432/experimental"
#conn = connections.get("default")

# async def no_param_query():
#     await Tortoise.init(db_url=DB_URL, modules={"models":[]})
    
#     #non parameters quiery
#     try:
        
#         counts, rows =  await conn.execute_query("SELECT * FROM app_user;")
#         print(counts)
#         print("-----------------")
#         print(rows)
#     finally:
#         await Tortoise.close_connections()


async def main():
    await Tortoise.init(db_url=DB_URL, modules={"models":[]})
    
    try:
        conn = connections.get("default")
        query ="SELECT * FROM app_user WHERE user_name=$1;"

        row_count, rows = await conn.execute_query(query, ["Samat"])

        print(row_count)
        print(rows)
    finally:
        await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(main())