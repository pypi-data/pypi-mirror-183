from .user import User as User
from .utils import Credential
from .video import Video as Video


class Anbiliapi:
    def __init__(self, credential: Credential) -> None:
        self.__credential = credential

    def get_user(self) -> User:
        return User(credential=self.__credential)

    def get_video(self, aid: int = None, bid: str = None) -> Video:
        return Video(credential=self.__credential, bid=bid, aid=aid)
