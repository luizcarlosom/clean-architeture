from .users_repository import UsersRepository

def test_insert_user():
    mocked_first_name = 'First'
    mocked_last_name = 'Last'
    mocked_age = 34

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_first_name, mocked_last_name, mocked_age)
