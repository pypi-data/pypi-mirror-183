from abc import ABC, abstractmethod
from requests import Response


class Connector(ABC):
    def __init__(self, target, username: str = "", password: str = ""):
        self.target = target
        self.username = username
        self.password = password

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ConnectorSSH(Connector):
    @abstractmethod
    def send_command(self):
        pass


class ConnectorAPI(Connector):
    @abstractmethod
    def get(self, uri: str, options: dict) -> Response:
        pass

    @abstractmethod
    def post(self, uri: str, options: dict) -> Response:
        pass

    @abstractmethod
    def put(self, uri: str, options: dict) -> Response:
        pass

    @abstractmethod
    def delete(self, uri: str, options: dict) -> Response:
        pass
