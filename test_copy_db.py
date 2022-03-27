import pytest
import allure
import config


ships_amount = config.ships_amount

@pytest.mark.parametrize('ship_number', [i for i in range(1, ships_amount + 1)])
class TestCopyDB():
    @allure.story('test weapon')
    def test_weapon(self, create_new_db, ship_number):
        cursor1, cursor2 = create_new_db
        
        cursor1.execute('SELECT * FROM Ships;')
        ship1 = cursor1.fetchall()[ship_number - 1]

        cursor2.execute('SELECT * FROM Ships;')
        ship2 = cursor2.fetchall()[ship_number - 1]

        cursor2.execute('SELECT * FROM weapons;')
        weapons2 = cursor2.fetchall()

        cursor2.execute('PRAGMA table_info(weapons);')
        weapons2_table_info = cursor2.fetchall()
        weapons2_columns = []
        for element in weapons2_table_info:
            weapons2_columns.append(element[1])
        
        weapon1_title = ship1[1]
        weapon2_title = ship2[1]

        weapon2_index = None
        weapon2 = None
        for i in range(len(weapons2)):
            if weapons2[i][0] == weapon2_title:
                weapon2_index = i
                weapon2 = weapons2[i]
        
        cursor1.execute('SELECT * FROM weapons;')
        weapons1 = cursor1.fetchall()
        weapon1 = weapons1[weapon2_index]
        
        with allure.step('compare weapons titles'):
            pytest.assume(weapon2_title == weapon1_title, f'''
                -----------------------------------------
                {ship2[0]}, {weapon2_title}
                    expected {weapon1_title}, was {weapon2_title}
                -----------------------------------------''')

        with allure.step('compare weapons parameters'):
            for i in range(len(weapon2)):
                pytest.assume(weapon2[i] == weapon1[i], f'''
                -----------------------------------------
                {ship2[0]}, {weapon2[0]}
                    {weapons2_columns[i]}: expected {weapon1[i]}, was {weapon2[i]}
                -----------------------------------------''')

    @allure.story('test hull')
    def test_hull(self, create_new_db, ship_number):
        cursor1, cursor2 = create_new_db
        
        cursor1.execute('SELECT * FROM Ships;')
        ship1 = cursor1.fetchall()[ship_number - 1]

        cursor2.execute('SELECT * FROM Ships;')
        ship2 = cursor2.fetchall()[ship_number - 1]

        cursor2.execute('SELECT * FROM hulls;')
        hulls2 = cursor2.fetchall()
        
        cursor2.execute('PRAGMA table_info(hulls);')
        hulls2_table_info = cursor2.fetchall()
        hulls2_columns = []
        for element in hulls2_table_info:
            hulls2_columns.append(element[1])
        
        hull1_title = ship1[2]
        hull2_title = ship2[2]

        hull2_index = None
        hull2 = None
        for i in range(len(hulls2)):
            if hulls2[i][0] == hull2_title:
                hull2_index = i
                hull2 = hulls2[i]
        
        cursor1.execute('SELECT * FROM hulls;')
        hulls1 = cursor1.fetchall()
        hull1 = hulls1[hull2_index]

        with allure.step('compare hulls titles'):
            pytest.assume(hull2_title == hull1_title, f'''
                -----------------------------------------
                {ship2[0]}, {hull2_title}
                    expected {hull1_title}, was {hull2_title}
                -----------------------------------------''')

        with allure.step('compare hulls parameters'):
            for i in range(len(hull2)):
                pytest.assume(hull2[i] == hull1[i], f'''
                -----------------------------------------
                {ship2[0]}, {hull2[0]}
                    {hulls2_columns[i]}: expected {hull1[i]}, was {hull2[i]}
                -----------------------------------------''')

    @allure.story('test engine')
    def test_engine(self, create_new_db, ship_number):
        cursor1, cursor2 = create_new_db
        
        cursor1.execute('SELECT * FROM Ships;')
        ship1 = cursor1.fetchall()[ship_number - 1]

        cursor2.execute('SELECT * FROM Ships;')
        ship2 = cursor2.fetchall()[ship_number - 1]

        cursor2.execute('SELECT * FROM engines;')
        engines2 = cursor2.fetchall()
        
        cursor2.execute('PRAGMA table_info(engines);')
        engines2_table_info = cursor2.fetchall()
        engines2_columns = []
        for element in engines2_table_info:
            engines2_columns.append(element[1])
        
        engine1_title = ship1[3]
        engine2_title = ship2[3]

        engine2_index = None
        engine2 = None
        for i in range(len(engines2)):
            if engines2[i][0] == engine2_title:
                engine2_index = i
                engine2 = engines2[i]
        
        cursor1.execute('SELECT * FROM engines;')
        engines1 = cursor1.fetchall()
        engine1 = engines1[engine2_index]

        with allure.step('compare engines titles'):
            pytest.assume(engine2_title == engine1_title, f'''
                -----------------------------------------
                {ship2[0]}, {engine2_title}
                    expected {engine1_title}, was {engine2_title}    
                -----------------------------------------''')

        with allure.step('compare engines parameters'):
            for i in range(len(engine2)):
                pytest.assume(engine2[i] == engine1[i], f'''
                -----------------------------------------
                {ship2[0]}, {engine2[0]}
                    {engines2_columns[i]}: expected {engine1[i]}, was {engine2[i]}
                -----------------------------------------''')
