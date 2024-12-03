import os
from dotenv import load_dotenv

load_dotenv()

AOC_YEAR = int(os.getenv("AOC_YEAR") or "-1")
AOC_TOKEN = os.getenv("AOC_TOKEN")
