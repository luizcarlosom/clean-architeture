import pytest
from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_register import UserRegister

def test_register():
    first_name = "Ola"
    last_name = "Mundo"
    age = 3

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    response = user_register.register(first_name, last_name, age)

    assert repo.insert_user_attributtes["first_name"] == first_name
    assert repo.insert_user_attributtes["last_name"] == last_name
    assert repo.insert_user_attributtes["age"] == age

    assert response["type"] == "Users"
    assert response["count"] == 1
    assert response["attributtes"]

def test_register_first_name_error():
    first_name = "123"
    last_name = "Mundo"
    age = 3

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    with pytest.raises(Exception) as exc_info:
        user_register.register(first_name, last_name, age)
    
    assert str(exc_info.value) == "Nome invalido para a busca"

def test_register_first_name_error_in_long_name():
    first_name = 'meuNomeEhLuizCarlosOliveiraMaciel'
    last_name = "Mundo"
    age = 3

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    with pytest.raises(Exception) as exc_info:
        user_register.register(first_name, last_name, age)
    
    assert str(exc_info.value) == "Nome muito grande para busca"
