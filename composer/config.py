import os
import re

SITE_DIR = "site"
BUILD_DIR = "build"
BUILD_DEV_DIR = "build-dev"
TEMPLATES_DIR = "site/templates"
DATA_DIR = "site/data"
RESOURCES_JSON = "site/data/resources.json"

SITE_URL = "https://school.gijs6.nl"
SITE_TITLE = "Samenvattingen :)"
SITE_DESCRIPTION = "Een verzameling van zelfgemaakte samenvattingen"
AUTHOR_NAME = "Gijs ten Berg"
AUTHOR_EMAIL = "me@gijs6.nl"

YEAR_DIR_PATTERN = re.compile(r"(\d)VWO")
PERIOD_PATTERN = re.compile(r"([A-Z]+)(\d+)")
ONDERBOUW_DIR = os.path.join(SITE_DIR, "onderbouw")
FRONT_MATTER_PATTERN = re.compile(r"^---\n(.*?)\n---", re.DOTALL)

SUBJECT_FAMILIES = {
    "ENTL": "talen",
    "FATL": "talen",
    "NETL": "talen",
    "BIOL": "bio",
    "NAT": "exact",
    "SCHK": "exact",
    "WISB": "wis",
    "NLT": "exact",
    "MAAT": "mens",
}

ONDERBOUW_FAMILIES = {
    "Duits": "talen",
    "Engels": "talen",
    "Frans": "talen",
    "Nederlands": "talen",
    "Biologie": "bio",
    "Natuurkunde": "exact",
    "Scheikunde": "exact",
    "Wiskunde": "wis",
    "NST": "exact",
    "Aardrijkskunde": "mens",
    "Economie": "mens",
    "Geschiedenis": "mens",
    "Beeldende Vorming": "kunst",
    "Muziek": "kunst",
}

SUBJECT_NAMES = {
    "BIOL": "Biologie",
    "ENTL": "Engels",
    "FATL": "Frans",
    "NETL": "Nederlands",
    "NAT": "Natuurkunde",
    "SCHK": "Scheikunde",
    "WISB": "Wiskunde B",
    "MAAT": "Maatschappijleer",
    "NLT": "NLT",
}
