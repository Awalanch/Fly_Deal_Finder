"""Base project settings."""

import os
from pathlib import Path

from decouple import AutoConfig

BASE_DIR = Path(__file__).resolve().parent.parent
config = AutoConfig(os.environ.get("ENV_FILE_PATH", f"{BASE_DIR}/settings/envs/.env"))
MY_EMAIL = config("MY_EMAIL")
MY_PASSWORD = config("MY_PASSWORD")
TEQUILA_API_KEY = config("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/9312aedc4fd63b80c4ed271a5f851f73/flightDeals/prices"
ORIGIN_CITI_IATA = "PRG"
