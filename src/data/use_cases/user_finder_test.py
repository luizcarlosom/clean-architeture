import pytest
from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_finder import UserFinder

def test_find():
    first_name = 'meuNome'

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find(first_name)

    assert repo.select_user_attributtes["first_name"] == first_name

    assert response["type"] == "Users"
    assert response["count"] == len(response["attributtes"])
    assert response["attributtes"]

def test_find_error_in_invalid_name():
    first_name = 'meuNome123'

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    with pytest.raises(Exception) as  exc_info:
        user_finder.find(first_name)

    assert str(exc_info.value) == "Nome invalido para a busca"

def test_find_error_in_long_name():
    first_name = 'meuNomeEhLuizCarlosOliveiraMaciel'

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    with pytest.raises(Exception) as  exc_info:
        user_finder.find(first_name)

    assert str(exc_info.value) == "Nome muito grande para busca"

def test_find_error_user_not_found():
    class UsersRepositoryError(UsersRepositorySpy):
        def select_user(self, first_name: str):
            return []
        
    first_name = 'meuNome'

    repo = UsersRepositoryError()
    user_finder = UserFinder(repo)

    with pytest.raises(Exception) as  exc_info:
        user_finder.find(first_name)

    assert str(exc_info.value) == "Usuario nao encontrado"
