import os
import sqlite3

from config.settings import settings
from utils.logger import logger


class MemoryDatabase:

    def __init__(self):

        os.makedirs(
            settings.DATA_DIRECTORY,
            exist_ok=True
        )

        self.connection = sqlite3.connect(
            settings.DATABASE_PATH,
            check_same_thread=False
        )

        self.create_tables()

        logger.info(
            "Memory database initialized"
        )

    def create_tables(self):

        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS memories (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                memory_type TEXT NOT NULL,

                key TEXT NOT NULL,

                value TEXT NOT NULL,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.connection.commit()

    def save_memory(
        self,
        memory_type,
        key,
        value
    ):

        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT id
            FROM memories
            WHERE memory_type = ?
            AND key = ?
        """, (
            memory_type,
            key
        ))

        existing = cursor.fetchone()

        if existing:

            cursor.execute("""
                UPDATE memories

                SET value = ?,
                    updated_at = CURRENT_TIMESTAMP

                WHERE id = ?
            """, (
                value,
                existing[0]
            ))

        else:

            cursor.execute("""
                INSERT INTO memories (
                    memory_type,
                    key,
                    value
                )

                VALUES (?, ?, ?)
            """, (
                memory_type,
                key,
                value
            ))

        self.connection.commit()

        logger.info(
            f"Memory saved: {memory_type} / {key}"
        )

        return True

    def get_memory(
        self,
        memory_type,
        key
    ):

        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT value
            FROM memories

            WHERE memory_type = ?
            AND key = ?
        """, (
            memory_type,
            key
        ))

        result = cursor.fetchone()

        if result:

            return result[0]

        return None

    def get_all_memories(
        self,
        memory_type=None
    ):

        cursor = self.connection.cursor()

        if memory_type:

            cursor.execute("""
                SELECT
                    memory_type,
                    key,
                    value

                FROM memories

                WHERE memory_type = ?

                ORDER BY updated_at DESC
            """, (
                memory_type,
            ))

        else:

            cursor.execute("""
                SELECT
                    memory_type,
                    key,
                    value

                FROM memories

                ORDER BY updated_at DESC
            """)

        return cursor.fetchall()