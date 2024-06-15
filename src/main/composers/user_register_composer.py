from src.infra.db.repositories.users_repository import UsersRepository
from src.data.use_cases.user_register import UserRegister
from src.presentation.controllers.user_register_controller import UserRegisterController

def user_register_composer():
    repository = UsersRepository()
    user_case = UserRegister(repository)
    controller = UserRegisterController(user_case)

    return controller.handle
