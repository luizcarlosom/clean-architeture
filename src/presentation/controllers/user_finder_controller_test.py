from src.presentation.controllers.user_finder_controller import UserFinderController
from src.data.tests.user_finder import UserFinderSpy
from src.presentation.http_types.http_response import HttpResponse

class HttpsRequestMock():
    def __init__(self) -> None:
        self.query_params = { "first_name": "meuTeste" }
        

def test_handle():
    http_request_mock = HttpsRequestMock()
    user_case = UserFinderSpy()
    user_finder_controller = UserFinderController(user_case)

    response = user_finder_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None
