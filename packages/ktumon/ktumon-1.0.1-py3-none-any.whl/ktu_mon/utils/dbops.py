import sqlite3
from sqlite3 import Connection, Cursor
from typing import Callable
from pathlib import Path
from ktu_mon.utils.constants import DB_NAME, PROC_ID_INITIALIZER


def db_init(time_func: Callable[[], str]) -> None:
    if Path(f"{DB_NAME}.db").is_file():
        print("Local DB exists! Skipping Initialisation.")
        raise Exception("DB EXISTS!")
    else:
        print("Local DB does not exist! Creating!")
        conn: Connection = sqlite3.connect(f"{DB_NAME}.db")
        cur: Cursor = conn.cursor()
        with conn:
            cur.execute(
                """CREATE TABLE log_temp (
                    notif_date text not null,
                    notification text not null,
                    cre_proc integer not null,
                    cre_proc_ts text not null,
                    upd_proc integer,
                    upd_proc_ts text,
                    trashed integer not null
                )"""
            )
            cur.execute(
                """CREATE TABLE logs (
                    notif_date text not null,
                    notification text not null,
                    cre_proc integer not null,
                    cre_proc_ts text not null,
                    upd_proc integer,
                    upd_proc_ts text,
                    trashed integer not null
                )"""
            )
            cur.execute(
                """CREATE TABLE log_dates (
                    notif_date text not null,
                    cre_proc integer not null,
                    cre_proc_ts text primary key,
                    upd_proc integer,
                    upd_proc_ts text,
                    trashed integer not null
                )"""
            )
            cur.execute(
                """CREATE TABLE config (
                    parameter text primary key,
                    value text,
                    cre_proc integer not null,
                    cre_proc_ts text not null,
                    upd_proc integer,
                    upd_proc_ts text
                )"""
            )
            cur.execute(
                """INSERT INTO config (
                    parameter,
                    value,
                    cre_proc,
                    cre_proc_ts,
                    upd_proc,
                    upd_proc_ts
                ) VALUES (
                    :parameter,
                    :value,
                    :cre_proc,
                    :cre_proc_ts,
                    :upd_proc,
                    :upd_proc_ts
                )""",
                {
                    "parameter": "time_interval",
                    "value": 30,
                    "cre_proc": PROC_ID_INITIALIZER,
                    "cre_proc_ts": time_func(),
                    "upd_proc": None,
                    "upd_proc_ts": None,
                },
            )
            cur.execute(
                """INSERT INTO config (
                    parameter,
                    value,
                    cre_proc,
                    cre_proc_ts,
                    upd_proc,
                    upd_proc_ts
                ) VALUES (
                    :parameter,
                    :value,
                    :cre_proc,
                    :cre_proc_ts,
                    :upd_proc,
                    :upd_proc_ts
                )""",
                {
                    "parameter": "last_checked",
                    "value": None,
                    "cre_proc": PROC_ID_INITIALIZER,
                    "cre_proc_ts": time_func(),
                    "upd_proc": None,
                    "upd_proc_ts": None,
                },
            )
            cur.execute(
                """INSERT INTO config (
                    parameter,
                    value,
                    cre_proc,
                    cre_proc_ts,
                    upd_proc,
                    upd_proc_ts
                ) VALUES (
                    :parameter,
                    :value,
                    :cre_proc,
                    :cre_proc_ts,
                    :upd_proc,
                    :upd_proc_ts
                )""",
                {
                    "parameter": "last_logged",
                    "value": None,
                    "cre_proc": PROC_ID_INITIALIZER,
                    "cre_proc_ts": time_func(),
                    "upd_proc": None,
                    "upd_proc_ts": None,
                },
            )
            cur.execute(
                """INSERT INTO config (
                    parameter,
                    value,
                    cre_proc,
                    cre_proc_ts,
                    upd_proc,
                    upd_proc_ts
                ) VALUES (
                    :parameter,
                    :value,
                    :cre_proc,
                    :cre_proc_ts,
                    :upd_proc,
                    :upd_proc_ts
                )""",
                {
                    "parameter": "notification_ind",
                    "value": "0",
                    "cre_proc": PROC_ID_INITIALIZER,
                    "cre_proc_ts": time_func(),
                    "upd_proc": None,
                    "upd_proc_ts": None,
                },
            )


def config_mod(parameter: str, value: str, proc_id: int, time_func: Callable[[], str]) -> None:
    conn: Connection = sqlite3.connect(f"{DB_NAME}.db")
    cur: Cursor = conn.cursor()
    with conn:
        cur.execute(
            """UPDATE config SET
                value = :value,
                upd_proc = :upd_proc,
                upd_proc_ts = :upd_proc_ts
                WHERE parameter = :parameter""",
            {
                "value": value,
                "parameter": parameter,
                "upd_proc": proc_id,
                "upd_proc_ts": time_func(),
            },
        )
    print(f"Config {parameter} set to {value}")


def insert_log(date: str, notification: str, proc_id: int, proc_ts: str, mode: str | None) -> None:
    conn: Connection = sqlite3.connect(f"{DB_NAME}.db")
    cur: Cursor = conn.cursor()
    with conn:
        if mode == "temp":
            cur.execute(
                """INSERT INTO log_temp (
                        notif_date,
                        notification,
                        cre_proc,
                        cre_proc_ts,
                        upd_proc,
                        upd_proc_ts,
                        trashed
                    ) VALUES (
                        :notif_date,
                        :notification,
                        :cre_proc,
                        :cre_proc_ts,
                        :upd_proc,
                        :upd_proc_ts,
                        :trashed
                    )""",
                {
                    "notif_date": date,
                    "notification": notification,
                    "cre_proc": proc_id,
                    "cre_proc_ts": proc_ts,
                    "upd_proc": None,
                    "upd_proc_ts": None,
                    "trashed": 0,
                },
            )
        else:
            cur.execute(
                """INSERT INTO logs (
                        notif_date,
                        notification,
                        cre_proc,
                        cre_proc_ts,
                        upd_proc,
                        upd_proc_ts,
                        trashed
                    ) VALUES (
                        :notif_date,
                        :notification,
                        :cre_proc,
                        :cre_proc_ts,
                        :upd_proc,
                        :upd_proc_ts,
                        :trashed
                    )""",
                {
                    "notif_date": date,
                    "notification": notification,
                    "cre_proc": proc_id,
                    "cre_proc_ts": proc_ts,
                    "upd_proc": None,
                    "upd_proc_ts": None,
                    "trashed": 0,
                },
            )


def insert_log_date(date, proc_id, proc_ts) -> None:
    conn: Connection = sqlite3.connect(f"{DB_NAME}.db")
    cur: Cursor = conn.cursor()
    with conn:
        cur.execute(
            """INSERT INTO log_dates (
                notif_date,
                cre_proc,
                cre_proc_ts,
                upd_proc,
                upd_proc_ts,
                trashed
            ) VALUES (
                :notif_date,
                :cre_proc,
                :cre_proc_ts,
                :upd_proc,
                :upd_proc_ts,
                :trashed
            )""",
            {
                "notif_date": date,
                "cre_proc": proc_id,
                "cre_proc_ts": proc_ts,
                "upd_proc": None,
                "upd_proc_ts": None,
                "trashed": 0,
            },
        )
        print(f"Inserted log dated {date}")


def trash_log(date, proc_id, time_func) -> None:
    conn: Connection = sqlite3.connect(f"{DB_NAME}.db")
    cur: Cursor = conn.cursor()
    with conn:
        cur.execute(
            """UPDATE logs SET
                trashed = 1,
                upd_proc = :upd_proc
                upd_proc_ts = :upd_proc_ts
                WHERE cre_proc_ts = :cre_proc_ts""",
            {
                "upd_proc": proc_id,
                "upd_proc_ts": time_func(),
                "cre_proc_ts": date,
            },
        )
        cur.execute(
            """UPDATE log_dates SET
                trashed = 1,
                upd_proc = :upd_proc
                upd_proc_ts = :upd_proc_ts
                WHERE cre_proc_ts = :cre_proc_ts""",
            {
                "upd_proc": proc_id,
                "upd_proc_ts": time_func(),
                "cre_proc_ts": date,
            },
        )
        print(f"Log dated {date} is now in trash")


def restore_log(date, proc_id, time_func) -> None:
    conn: Connection = sqlite3.connect(f"{DB_NAME}.db")
    cur: Cursor = conn.cursor()
    with conn:
        cur.execute(
            """UPDATE logs SET
                trashed = 0,
                upd_proc = :upd_proc
                upd_proc_ts = :upd_proc_ts
                WHERE cre_proc_ts = :cre_proc_ts""",
            {
                "upd_proc": proc_id,
                "upd_proc_ts": time_func(),
                "cre_proc_ts": date,
            },
        )
        cur.execute(
            """UPDATE log_dates SET
                trashed = 0,
                upd_proc = :upd_proc
                upd_proc_ts = :upd_proc_ts
                WHERE cre_proc_ts = :cre_proc_ts""",
            {
                "upd_proc": proc_id,
                "upd_proc_ts": time_func(),
                "cre_proc_ts": date,
            },
        )
        print(f"Log dated {date} is now restored from trash")


def delete_log(date, mode) -> None:
    conn: Connection = sqlite3.connect(f"{DB_NAME}.db")
    cur: Cursor = conn.cursor()
    with conn:
        if mode == "temp":
            cur.execute(
                """DELETE from log_temp WHERE cre_proc_ts = :cre_proc_ts""",
                {
                    "cre_proc_ts": date,
                },
            )
            print(f"Temporary log cache dated {date} cleared")
        else:
            cur.execute(
                """DELETE from logs WHERE cre_proc_ts = :cre_proc_ts""",
                {
                    "cre_proc_ts": date,
                },
            )
            cur.execute(
                """DELETE from log_dates WHERE cre_proc_ts = :cre_proc_ts""",
                {
                    "cre_proc_ts": date,
                },
            )
            print(f"Log dated {date} is permanently deleted")


def fetch_log_list(trashed) -> list:
    conn: Connection = sqlite3.connect(f"{DB_NAME}.db")
    cur: Cursor = conn.cursor()
    with conn:
        cur.execute(
            """SELECT * FROM log_dates where trashed = :trashed ORDER BY notif_date DESC""",
            {"trashed": trashed},
        )
        return cur.fetchall()


def fetch_log(cre_proc_ts, mode) -> list:
    conn: Connection = sqlite3.connect(f"{DB_NAME}.db")
    cur: Cursor = conn.cursor()
    with conn:
        if mode == "temp":
            cur.execute(
                """SELECT * FROM log_temp where cre_proc_ts = :cre_proc_ts""",
                {"cre_proc_ts": cre_proc_ts},
            )
        else:
            cur.execute(
                """SELECT * FROM logs where cre_proc_ts = :cre_proc_ts""",
                {"cre_proc_ts": cre_proc_ts},
            )
        return cur.fetchall()


def fetch_config(key) -> list:
    conn: Connection = sqlite3.connect(f"{DB_NAME}.db")
    cur: Cursor = conn.cursor()
    with conn:
        cur.execute(
            """SELECT * FROM config where parameter = :parameter""",
            {"parameter": key},
        )
        return cur.fetchall()


def fetch_comp(left_ts, right_ts, mode) -> list:
    conn: Connection = sqlite3.connect(f"{DB_NAME}.db")
    cur: Cursor = conn.cursor()
    with conn:
        if mode == "temp":
            cur.execute(
                """SELECT _left.notif_date as notification_ts,
                _left.notification as _left,
                _right.notification as _right
                FROM (SELECT * FROM log_temp) as _left
                LEFT JOIN (SELECT * FROM logs WHERE cre_proc_ts=:right_ts) as _right
                ON _left.notification=_right.notification AND _left.notif_date=_right.notif_date
                UNION ALL
                SELECT _right.notif_date as notification_ts,
                _left.notification as _left,
                _right.notification as _right
                FROM (SELECT * FROM logs WHERE cre_proc_ts=:right_ts) as _right
                LEFT JOIN (SELECT * FROM log_temp) as _left
                ON _left.notification=_right.notification AND _left.notif_date=_right.notif_date
                WHERE _left.cre_proc_ts IS NULL
                ORDER BY notification_ts DESC
                """,
                {"right_ts": right_ts},
            )
        else:
            cur.execute(
                """SELECT _left.notif_date as notification_ts,
                _left.notification as _left,
                _right.notification as _right
                FROM (SELECT * FROM logs WHERE cre_proc_ts=:left_ts) as _left
                LEFT JOIN (SELECT * FROM logs WHERE cre_proc_ts=:right_ts) as _right
                ON _left.notification=_right.notification AND _left.notif_date=_right.notif_date
                UNION ALL
                SELECT _right.notif_date as notification_ts,
                _left.notification as _left,
                _right.notification as _right
                FROM (SELECT * FROM logs WHERE cre_proc_ts=:right_ts) as _right
                LEFT JOIN (SELECT * FROM logs WHERE cre_proc_ts=:left_ts) as _left
                ON _left.notification=_right.notification AND _left.notif_date=_right.notif_date
                WHERE _left.cre_proc_ts IS NULL
                ORDER BY notification_ts DESC
                """,
                {"left_ts": left_ts, "right_ts": right_ts},
            )
        return cur.fetchall()
