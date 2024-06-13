from typing import Dict

class UserFinderSpy:
    def __init__(self) -> None:
        self.find_attributtes = {}

    def find(self, first_name: str) -> Dict:
        self.find_attributtes["first_name"] = first_name

        return {
            "type": "Users",
            "count": 1,
            "attributtes": [
                {"first_name": first_name, "last_name": "something"}
            ]
        }
