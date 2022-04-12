import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    print("File .env not found!")

TALENTS_FILENAME = os.getenv("TALENTS_FILENAME") or "talents.json"
TALENTS_FILE_PATH = os.path.join(dirname, "..", "data", TALENTS_FILENAME)

ARCHETYPES_FILENAME = os.getenv("ARCHETYPES_FILENAME") or "archetypes.json"
ARCHETYPES_FILE_PATH = os.path.join(dirname, "..", "data", ARCHETYPES_FILENAME)

NONEXISTING_FILENAME = os.getenv(
    "NONEXISTING_FILENAME") or "non-existing.json"
NONEXISTING_FILE_PATH = os.path.join(
    dirname, "..", "data", NONEXISTING_FILENAME)