import os
import random
from dataclasses import asdict, dataclass, field
from hashlib import md5
from time import time

import pandas as pd
from dacite import from_dict
from twilio.rest import Client

from gandai.datastore import Cloudstore
from gandai.models.User import user_exists

ds = Cloudstore()
twilio_client = Client(
    ds["env/TWILIO_APP"], 
    ds["env/TWILIO_TOKEN"]
)


@dataclass
class Auth:
    key: str = field(init=False)
    phone: str
    code: int  # 6 digit
    expires: int = field(init=False)
    token: str = field(init=False)

    def __post_init__(self):
        assert len(self.code) == 6
        self.expires = int(time()) + (7 * 86400)
        self.key = f"auth/{self.phone}/{self.expires}"
        self.token = md5(self.key.encode()).hexdigest()


def _send_code(auth: Auth) -> None:
    message = twilio_client.messages.create(
        to=auth.phone,
        from_=ds["env/TWILIO_NUMBER"],
        body=f"Your Login Code is: {auth.code}",
    )
    print(f"Login Sent to {auth.phone}")


def send_code(phone: str) -> int:
    # should 
    # a) anyone be able to do a 2FA?, OR
    # b) only exisiting users?
    if user_exists(phone):
        auth_code = random.randint(100000, 999999)
        auth = Auth(phone=phone, code=auth_code)
        _send_code(auth)
        ds[auth.key] = asdict(auth)
        return 200
    else:
        print("Nah")
        return 401


def authenticate(code: int) -> str:
    for k in ds.keys("auth"):
        auth = from_dict(Auth, ds[k])
        if code == auth.code and auth.expires > int(time()):
            return auth.token


def validate(token: str) -> bool:
    pass
