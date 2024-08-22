class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(self, title: str, duration: int):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = False

class UrTube:
    def __init__(self):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):

