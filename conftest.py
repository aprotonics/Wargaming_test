import sqlite3
import random
import pytest
import allure
import config


int_range = config.int_range

@pytest.fixture(scope='session')
def create_new_db():
    ### initialize
    with allure.step('Initialize connection'):
        connection1 = sqlite3.connect('ships.db')
        cursor1 = connection1.cursor()

    ### fetch db
    with allure.step('Fetch database'):
        # ships
        cursor1.execute('SELECT * FROM Ships;')
        ships = cursor1.fetchall()

        # weapons
        cursor1.execute('SELECT * FROM weapons;')
        weapons = cursor1.fetchall()

        # hulls
        cursor1.execute('SELECT * FROM hulls;')
        hulls = cursor1.fetchall()

        # engines
        cursor1.execute('SELECT * FROM engines;')
        engines = cursor1.fetchall()

    ### randomize values
    with allure.step('Randomize values'):
        # ships
        new_ships = []
        for ship_tuple in ships:
            ship_list = []
            random_component_number = random.randint(1, 3)
            DICT = {
                1: weapons,
                2: hulls,
                3: engines
            }
            for i in range(len(ship_tuple)):
                element = ship_tuple[i]
                if i == random_component_number:
                    while element == ship_tuple[i]: # do while random element will not differ from initial value 
                        element = random.choice(DICT[i])[0]
                ship_list.append(element)

            new_ships.append(ship_list)

        # weapons
        new_weapons = []
        for weapon_tuple in weapons:
            weapon_list = []
            random_parameter_number = random.randint(1, 5)
            for i in range(len(weapon_tuple)):
                element = weapon_tuple[i]
                if i == random_parameter_number:
                    while element == weapon_tuple[i]: # do while random element will not differ from initial value 
                        element = random.randint(int_range[0], int_range[1])
                weapon_list.append(element)
            new_weapons.append(weapon_list)

        # hulls
        new_hulls = []
        for hull_tuple in hulls:
            hull_list = []
            random_parameter_number = random.randint(1, 3)
            for i in range(len(hull_tuple)):
                element = hull_tuple[i]
                if i == random_parameter_number:
                    while element == hull_tuple[i]: # do while random element will not differ from initial value 
                        element = random.randint(int_range[0], int_range[1])
                hull_list.append(element)
            new_hulls.append(hull_list)

        # engines
        new_engines = []
        for engine_tuple in engines:
            engine_list = []
            random_parameter_number = random.randint(1, 2)
            for i in range(len(engine_tuple)):
                element = engine_tuple[i]
                if i == random_parameter_number:
                    while element == engine_tuple[i]: # do while random element will not differ from initial value 
                        element = random.randint(int_range[0], int_range[1])
                engine_list.append(element)
            new_engines.append(engine_list)

    ### create new db
    with allure.step('Create new database'):
        connection2 = sqlite3.connect(':memory:')
        cursor2 = connection2.cursor()

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
        cursor2.execute(SQL)
        connection2.commit()

        # hulls
        SQL = '''CREATE TABLE IF NOT EXISTS hulls(
            hull TEXT PRIMARY KEY,
            armor INTEGER,
            type INTEGER,
            capacity INTEGER
        );
        '''
        cursor2.execute(SQL)
        connection2.commit()

        # engines
        SQL = '''CREATE TABLE IF NOT EXISTS engines(
            engine TEXT PRIMARY KEY,
            power INTEGER,
            type INTEGER
        );
        '''
        cursor2.execute(SQL)
        connection2.commit()

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
        cursor2.execute(SQL)
        connection2.commit()

    ### fill database
    with allure.step('Fill new database'):
        # weapons
        SQL = 'INSERT INTO weapons VALUES(?, ?, ?, ?, ?, ?);'
        cursor2.executemany(SQL, new_weapons)
        connection2.commit()

        # hulls
        SQL = 'INSERT INTO hulls VALUES(?, ?, ?, ?);'
        cursor2.executemany(SQL, new_hulls)
        connection2.commit()

        # engines
        SQL = 'INSERT INTO engines VALUES(?, ?, ?);'
        cursor2.executemany(SQL, new_engines)
        connection2.commit()

        # ships
        SQL = 'INSERT INTO Ships VALUES(?, ?, ?, ?);'
        cursor2.executemany(SQL, new_ships)
        connection2.commit()

    return cursor1, cursor2
