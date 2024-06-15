from src.infra.db.repositories.users_repository import UsersRepository
from src.data.use_cases.user_finder import UserFinder
from src.presentation.controllers.user_finder_controller import UserFinderController

def user_register_composer():
    repository = UsersRepository()
    user_case = UserFinder(repository)
    controller = UserFinderController(user_case)

    return controller.handle
