import os
import re
from zoneinfo import ZoneInfo

SITE_DIR = "site"
ASSETS_DIR = os.path.join(SITE_DIR, "assets")
DATA_DIR = os.path.join(SITE_DIR, "data")
TEMPLATES_DIR = os.path.join(SITE_DIR, "templates")
ONDERBOUW_DIR = os.path.join(SITE_DIR, "onderbouw")
FAVICON = os.path.join(SITE_DIR, "favicon.ico")
RESOURCES_JSON = os.path.join(DATA_DIR, "resources.json")
COMPOSER_DIR = os.path.relpath(os.path.dirname(os.path.abspath(__file__)))

BUILD_DIR = "build"
BUILD_DEV_DIR = "build-dev"

SITE_URL = "https://school.gijs6.nl"
SITE_TITLE = "Samenvattingen :)"
SITE_DESCRIPTION = "Een verzameling van zelfgemaakte samenvattingen"
AUTHOR_NAME = "Gijs ten Berg"
AUTHOR_EMAIL = "me@gijs6.nl"
REPO_URL = "https://github.com/Gijs6/school.gijs6.nl"
TIMEZONE = ZoneInfo("Europe/Amsterdam")

YEAR_DIR_PATTERN = re.compile(r"(\d)VWO")
PERIOD_PATTERN = re.compile(r"([A-Z]+)(\d+)")

SUBJECTS = {
    "BIOL": ("Biologie", "bio"),
    "ENTL": ("Engels", "talen"),
    "FATL": ("Frans", "talen"),
    "NETL": ("Nederlands", "talen"),
    "NAT": ("Natuurkunde", "exact"),
    "SCHK": ("Scheikunde", "exact"),
    "WISB": ("Wiskunde B", "wis"),
    "MAAT": ("Maatschappijleer", "mens"),
    "NLT": ("NLT", "exact"),
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
    "Beeldende Vorming": "mens",
    "Muziek": "mens",
}
