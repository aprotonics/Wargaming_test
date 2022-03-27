import sqlite3
import random
import config


ships_amount = config.ships_amount
weapons_amount = config.weapons_amount
hulls_amount = config.hulls_amount
engines_amount = config.engines_amount
int_range = config.int_range

### initialize
connection = sqlite3.connect('ships.db')
cursor = connection.cursor()

### create database
# weapons
SQL = '''CREATE TABLE IF NOT EXISTS weapons(
    weapon TEXT PRIMARY KEY,
    reload_speed INTEGER,
    rotational_speed INTEGER,
    diameter INTEGER,
    power_volley INTEGER,
    count INTEGER
);
'''
cursor.execute(SQL)
connection.commit()

# hulls
SQL = '''CREATE TABLE IF NOT EXISTS hulls(
    hull TEXT PRIMARY KEY,
    armor INTEGER,
    type INTEGER,
    capacity INTEGER
);
'''
cursor.execute(SQL)
connection.commit()

# engines
SQL = '''CREATE TABLE IF NOT EXISTS engines(
    engine TEXT PRIMARY KEY,
    power INTEGER,
    type INTEGER
);
'''
cursor.execute(SQL)
connection.commit()

# ships
SQL = '''CREATE TABLE IF NOT EXISTS Ships(
    ship TEXT PRIMARY KEY,
    weapon TEXT NOT NULL,
    hull TEXT NOT NULL,
    engine TEXT NOT NULL,
    FOREIGN KEY (weapon)  REFERENCES weapons (weapon),
    FOREIGN KEY (hull)  REFERENCES hulls (hull),
    FOREIGN KEY (engine)  REFERENCES engines (engine)
);
'''
cursor.execute(SQL)
connection.commit()

### fill database
# create weapons values
weapons_list = []
for i in range(1, weapons_amount + 1):
    weapons_tuple = (
        f'Weapon-{i}',
        random.randint(int_range[0], int_range[1]),
        random.randint(int_range[0], int_range[1]),
        random.randint(int_range[0], int_range[1]),
        random.randint(int_range[0], int_range[1]),
        random.randint(int_range[0], int_range[1]))
    weapons_list.append(weapons_tuple)

# create hulls values
hulls_list = []
for i in range(1, hulls_amount + 1):
    hulls_tuple = (
        f'Hull-{i}',
        random.randint(int_range[0], int_range[1]),
        random.randint(int_range[0], int_range[1]),
        random.randint(int_range[0], int_range[1]))
    hulls_list.append(hulls_tuple)

# create engines values
engines_list = []
for i in range(1, engines_amount + 1):
    engine_tuple = (
        f'Engine-{i}',
        random.randint(int_range[0], int_range[1]),
        random.randint(int_range[0], int_range[1]))
    engines_list.append(engine_tuple)

# create ships values
ships_list = []
for i in range(1, ships_amount + 1):
    ships_tuple = (
        f'Ship-{i}',
        f'Weapon-{random.randint(1, weapons_amount)}',
        f'Hull-{random.randint(1, hulls_amount)}',
        f'Engine-{random.randint(1, engines_amount)}')
    ships_list.append(ships_tuple)

# create SQL-requests
SQL = 'INSERT INTO weapons VALUES(?, ?, ?, ?, ?, ?);'
cursor.executemany(SQL, weapons_list)
connection.commit()

SQL = 'INSERT INTO hulls VALUES(?, ?, ?, ?);'
cursor.executemany(SQL, hulls_list)
connection.commit()

SQL = 'INSERT INTO engines VALUES(?, ?, ?);'
cursor.executemany(SQL, engines_list)
connection.commit()

SQL = 'INSERT INTO Ships VALUES(?, ?, ?, ?);'
cursor.executemany(SQL, ships_list)
connection.commit()
