from dataclasses import asdict, dataclass, field
from time import time


@dataclass
class Comment:
    user: str  #
    body: str
    foreign_key: str
    created: int = field(init=False)
    key: str = field(init=False)

    def __post_init__(self):
        self.created = int(time())
        self.key = f"searches/{self.search_key}/comments/{self.created}"
