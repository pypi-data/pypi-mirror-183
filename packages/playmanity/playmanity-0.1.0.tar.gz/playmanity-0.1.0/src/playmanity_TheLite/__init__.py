import asyncio

import requests
try:
    from typing import NamedTuple, Literal
except ImportError:
    from typing_extensions import NamedTuple, Literal

__title__ = 'playmanity'
__author__ = 'TheLite'
__license__ = 'MIT'
__copyright__ = 'Copyright 2022-present TheLite & BetterPlaymanity'
__version__ = '0.1.0a'


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(major=0, minor=1, micro=0, releaselevel='alpha', serial=0)

class account():
    def __init__(self, nickname:str, password:str, about:str=None):
        self.nickname = nickname
        self.password = password
        self.token = ""
        self.about = about

    def run(self):
        req = requests.post('https://api.playmanity.com/sign-in', json={"username": self.nickname, "password": self.password})
        try:
            len(req["value"])
            self.token = req["value"]

            if self.about is not None:
                req = requests.patch('https://api.playmanity.com/user/profile', headers={"Authorization": req["value"]}, json={"name":self.nickname,"about":self.about})
                
        except:
            print("Failed to log in")

class profile:
    def __init__(self, nickname:str, about:str|None, avatar:str|None, background:str|None):
        self.nickname = nickname
        self.about = about
        self.avatar = avatar
        self.background = background

class get():
    def __init__(self):
        pass

    def profile(id):
        req = requests.get(f"https://api.playmanity.com/user/{id}/profile")
        if req.status_code == 200:
            req = req.json()
            return profile(req["username"],req["about"],req["avatarUrl"], req["backgroundUrl"])
        
        else:
            return req.text