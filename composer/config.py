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
ARCHIVE_DIR_PATTERN = re.compile(r"[23]VWO")
PERIOD_PATTERN = re.compile(r"([A-Z]+)(\d+)")
FRONT_MATTER_PATTERN = re.compile(r"^---\n(.*?)\n---", re.DOTALL)

SUBJECT_ICONS = {
    "BIOL": "fa-solid fa-seedling",
    "ENTL": "ENTL",
    "FATL": "FATL",
    "NETL": "NETL",
    "NAT": "fa-solid fa-atom",
    "SCHK": "fa-solid fa-flask-vial",
    "WISB": "fa-solid fa-calculator",
    "MAAT": "fa-solid fa-people-group",
    "NLT": "fa-solid fa-microscope",
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
