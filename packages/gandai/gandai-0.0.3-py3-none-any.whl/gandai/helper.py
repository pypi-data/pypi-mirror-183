import asyncio
import re
from collections import Counter

# import mapply
import pandas as pd
import plotly.express as px
from nltk import RegexpTokenizer, ngrams
from nltk.corpus import stopwords
from scipy.special import softmax
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler

from gandai.datastore import Cloudstore

ds = Cloudstore()

# mapply.init(n_workers=-1, chunk_size=1, max_chunks_per_worker=8, progressbar=False)


def dealcloud_query():
    df = pd.read_feather("data/dealcloud_export.feather")
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]
    return df


def _to_tokens(txt: str) -> list:
    tokenizer = RegexpTokenizer(r"\w+")
    tokens = tokenizer.tokenize(txt)
    lower_tokens = [t.lower() for t in tokens]
    clean = [t for t in lower_tokens if t not in stopwords.words("english")]
    return clean


def _to_ngram(tokens: list, n=2):
    grams = list(ngrams(tokens, 2))
    return [" ".join(list(gram)) for gram in grams]


def _to_ngrams(txt: str) -> list:
    if txt:
        tokens = _to_tokens(txt)
        grams: list = tokens
        grams.extend(_to_ngram(tokens, 2))
        grams.extend(_to_ngram(tokens, 3))
        return grams
    else:
        return []


def _get_match_ngrams(row) -> list:
    grams = []
    grams.extend(_to_ngrams(row["company_name"]))
    grams.extend(_to_ngrams(row["domain"]))
    grams.extend(_to_ngrams(row["business_description"]))
    grams.extend(_to_ngrams(row["main_industry"]))
    return grams


def _clean_days_since(txt):
    if txt:
        return int(re.findall(r"\d+", txt)[0])


def _get_domain(url) -> str:
    try:
        tokens = []
        for el in url.split("."):
            tokens.extend(el.split("/"))
        tld_index = tokens.index("com")
        domain_tokens = tokens[tld_index - 1 : tld_index + 1]
        domain = ".".join(domain_tokens)
        return domain
    except Exception as e:
        # print(e)
        pass


def _get_tld(url) -> str:
    tlds = [
        ".com",
        ".net",
        ".us",
        ".io",
        ".ca",
        ".uk",
        ".org",
        ".ai",
        ".biz",
        ".co",
        ".md",
        ".de",
        ".pharmacy",
        ".agency",
        ".solutions",
        ".global",
        ".eu",
    ]
    for tld in tlds:
        if tld in url:
            return tld
    return "?"


def dealcloud_feature_query():
    return_cols = [
        "company_name",
        "type",
        # "website",
        "domain",
        "business_description",
        "main_industry",
        # "linkedin",
        # "employee_linkedin_range",
        # "year_founded",
        # "employees",
        # "import_date",
        # "products",
        # "services",
        # "coverage_status",
        "days_since_contact",
        "zip5",
        "lat",
        "lon",
        "_ngrams",
        "_rev",
        "_employees",
    ]

    df = dealcloud_query()
    print(len(df))
    df["days_since_contact"] = df["days_since_contact"].apply(_clean_days_since)
    df["domain"] = df["website"].apply(_get_domain)
    df["tld"] = df["website"].dropna().apply(_get_tld)
    df["zip5"] = df["usa_postal_code"].dropna().apply(lambda x: str(x)[0:5])

    census = pd.read_feather("data/acs_zip5.feather")[["zip5", "lat", "lon"]]
    df = df.merge(census, how="left")

    # only recent
    # df = df[df["coverage_status"] != "Never Contacted"]

    df["_rev"] = df["source_revenue_(m)"]
    df = df.dropna(subset=["_rev"])
    df = df[df["_rev"] > 0]
    df = df[df["_rev"] < (10**3)]

    df["_employees"] = df["employees"]
    df = df.dropna(subset=["domain"])
    print(len(df))

    print("ngrams enabled... will take a min...")
    # df['_ngrams'] = df.mapply(_get_match_ngrams, axis=1)

    # df = df.sort_values("days_since_contact")
    return df[return_cols].reset_index(drop=True)
