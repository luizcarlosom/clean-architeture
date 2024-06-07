import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from .users_repository import UsersRepository

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip(reason="Sensive teste")
def test_insert_user():
    mocked_first_name = 'First'
    mocked_last_name = 'Last'
    mocked_age = 51

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_first_name, mocked_last_name, mocked_age)

    sql = '''
        SELECT * FROM users
        WHERE first_name = '{}'
        AND last_name = '{}'
        AND age = {} 
    '''.format(mocked_first_name, mocked_last_name, mocked_age)
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.first_name == mocked_first_name
    assert registry.last_name == mocked_last_name
    assert registry.age == mocked_age

    connection.execute(text(f'''
        DELETE FROM users WHERE id = {registry.id}
    ''')) 
    connection.commit()  

@pytest.mark.skip(reason="Sensive teste")
def test_select_user():
    mocked_first_name = 'First_2'
    mocked_last_name = 'Last_2'
    mocked_age = 51

    sql = '''
        INSERT INTO users (first_name, last_name, age) VALUES ('{}', '{}', '{}')
    '''.format(mocked_first_name, mocked_last_name, mocked_age)

    connection.execute(text(sql))
    connection.commit()

    users_repository = UsersRepository()
    response = users_repository.select_user(mocked_first_name)

    assert response[0].first_name == mocked_first_name
    assert response[0].last_name == mocked_last_name
    assert response[0].age == mocked_age

    connection.execute(text(f'''
        DELETE FROM users WHERE id = {response[0].id}
    ''')) 
    connection.commit()
