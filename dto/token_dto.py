from common.dto_decoder import DtoEncoder
from common.data_generator import random_string
from common.time_generator import get_current_unix_time


@DtoEncoder
class TokenDto:
    def __init__(self, resource_name: str):
        self.token_type: str = "Bearer"
        self.expires_in: str = "3599"
        self.ext_expires_in: str = "3599"
        self.expires_on: str = str(get_current_unix_time(int(self.expires_in)))
        self.not_before: str = str(get_current_unix_time())
        self.resource: str = resource_name
        self.access_token: str = self.get_access_token()

    @staticmethod
    def get_access_token() -> str:
        access_token: str = ""
        string_size_list: list = [132, 792, 342]
        for current_size in string_size_list:
            access_token: str = access_token + random_string(current_size) + "."
        return access_token
