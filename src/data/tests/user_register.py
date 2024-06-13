from typing import Dict

class UserRegisterSpy:
    def __init__(self) -> None:
        self.find_attributtes = {}

    def register(self, first_name: str, last_name: str, age: int) -> Dict:       
        self.find_attributtes["first_name"] = first_name
        self.find_attributtes["last_name"] = last_name
        self.find_attributtes["age"] = age

        return {
            "type": "Users",
            "count": 1,
            "attributtes": {
                "first_name": first_name,
                "last_name": last_name,
                "age": age
            }
        }
