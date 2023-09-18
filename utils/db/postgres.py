from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(
        self,
        command,
        *args,
        fetch: bool = False,
        fetchval: bool = False,
        fetchrow: bool = False,
        execute: bool = False,
    ):
        
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_cats(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Categories (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        parent_id BIGINT NULL
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_products(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        description TEXT NOT NULL,
        image_url VARCHAR(255) NOT NULL,
        price NUMERIC NOT NULL,
        category_id BIGINT NOT NULL
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_carts(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Cart (
        id SERIAL PRIMARY KEY,
        user_id BIGINT NOT NULL
        );
        """
        await self.execute(sql, execute=True)
    
    async def create_table_cart_items(self):
        sql = """
        CREATE TABLE IF NOT EXISTS CartItem (
        id SERIAL PRIMARY KEY,
        cart_id BIGINT NOT NULL,
        product_id BIGINT NOT NULL,
        quantity BIGINT NOT NULL
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    async def add_user(self, full_name, username, telegram_id):
        sql = "INSERT INTO users (full_name, username, telegram_id) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)
    
    async def add_cart(self, user_id):
        sql = "INSERT INTO Cart (user_id) VALUES($1) returning *"
        return await self.execute(sql, user_id, fetchrow=True)
    
    async def add_cart_items(self, cart_id, product_id, quantity):
        sql = "INSERT INTO CartItem (cart_id, product_id, quantity) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, cart_id, product_id, quantity, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)
    
    async def select_all_cats(self):
        sql = "SELECT * FROM Categories WHERE parent_id IS NULL;"
        return await self.execute(sql, fetch=True)
    
    async def select_cats_by_parent_id(self, parent_id):
        sql = "SELECT * FROM Categories WHERE parent_id=$1;"
        return await self.execute(sql, parent_id, fetch=True)
    
    async def select_product_by_category(self, category_id):
        sql = "SELECT * FROM Products WHERE category_id=$1;"
        return await self.execute(sql, category_id, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    
    async def select_cart(self, **kwargs):
        sql = "SELECT * FROM Cart WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    
    async def select_cart_item(self, **kwargs):
        sql = "SELECT * FROM CartItem WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    
    async def select_category(self, **kwargs):
        sql = "SELECT * FROM Categories WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    
    async def select_product(self, **kwargs):
        sql = "SELECT * FROM Products WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE Users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)
    
    async def update_cart_item_quantity(self, new_quantity, cart_id, product_id):
        sql = "UPDATE CartItem SET quantity=$1 WHERE cart_id=$2 AND product_id=$3"
        return await self.execute(sql, new_quantity, cart_id, product_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)
