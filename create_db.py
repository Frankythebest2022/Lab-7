"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import sqlite3
from datetime import datetime
from faker import Faker

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    create_ppl_tbl_query = """
    CREATE TABLE IF NOT EXISTS people
    (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        address TEXT NOT NULL,
        city TEXT NOT NULL,
        province TEXT NOT NULL,
        bio TEXT,
        age INTEGER,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL
    );
    """
    cur.execute(create_ppl_tbl_query)
    con.commit()
    con.close()

def populate_people_table():
    """Populates the people table with 200 fake people"""
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    add_person_query = """
    INSERT INTO people
    (
        name,
        email,
        address,
        city,
        province,
        bio,
        age,
        created_at,
        updated_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """

    fake = Faker()
    for _ in range(200):
        new_person = (
            fake.name(),
            fake.email(),
            fake.address(),
            fake.city(),
            fake.state(),
            fake.text(),
            fake.random_int(min=1, max=100),
            datetime.now(),
            datetime.now()
        )
        cur.execute(add_person_query, new_person)

    con.commit()
    con.close()

if __name__ == '__main__':
    main()