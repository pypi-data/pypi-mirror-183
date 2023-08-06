from dataclasses import asdict, dataclass, field
from typing import List

import pandas as pd

from gandai.datastore import Cloudstore
from gandai.models import Event
from gandai.services import Query

ds = Cloudstore()

# @dataclass
class Search:
    def __init__(self, key) -> None:
        self.key = key

    # client_key: str
    # start_date: str # iso_date
    # strategy: str  # "$4m health food manufacturing for pets"

    # def __post_init__(self):
    # self.key = f"searches/{self.search_key}/events/{self.created}"


# def load_targets(key: str) -> Search:


@dataclass
class SearchData:
    search_key: str


def load_search(search_key: str, actor_key: str) -> SearchData:
    Event.post_event(
        actor_key=actor_key, search_key=search_key, domain="", type="search"
    )
    companies = Query.companies_query(search_key)
    events = Query.events_query(search_key)
    df = companies.merge(
        events[["domain", "type"]], left_on="domain", right_on="domain", how="left"
    )

    def _json_safe(df):
        return df.fillna("").to_dict(orient="records")

    inbox = _json_safe(df[df["type"].isna()])
    reviewed = _json_safe(df[df["type"] == "advance"])
    qualified = _json_safe(df[df["type"] == "qualify"])
    rejected = _json_safe(df[df["type"] == "reject"])

    resp = {
        "search_key": search_key,
        "actor_key": actor_key,
        "meta": {
            "inbox": len(inbox),
            "review": len(reviewed),
            "qualified": len(qualified),
            "rejected": len(rejected),
        },
        "companies": {
            "inbox": inbox,
            "review": reviewed,
            "qualified": qualified,
            "rejected": rejected,
        },
    }
    return resp

    # search_key = "AXZ-144RV"
    # company_keys = ds.keys(f"searches/{search_key}/companies")
    # all_domains = set([k.split("/")[-1] for k in company_keys])

    # event_keys = ds.keys(f"searches/{search_key}/events")
    # events = pd.DataFrame([ds[k] for k in event_keys])
    # # print(events)

    # evaluated = set()#set(events["domain"])

    # remaining_domains = list(all_domains - evaluated)[0:10]

    # companies = [ds[k] for k in company_keys if k.split("/")[-1] in remaining_domains]
    # # df = pd.DataFrame(companies)
    # # df['employee_count'] = df['employees'].apply(lambda x: x.get("value"))
    # # df = df.sort_values("employee_count", ascending=False)

    # resp = {
    #     "search_key": search_key,
    #     "actor_key": actor_key,
    #     "meta": {
    #         "inbox": len(companies),
    #         "reviewed": 17,
    #         "qualified": 3,
    #         # "...": len(events),
    #     },
    #     "companies": {
    #         "inbox": companies,
    #         "reviewed": [],
    #         "qualified": [],
    #     },
    # }
    # return resp
