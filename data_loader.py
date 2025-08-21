import json
from pathlib import Path
from models import Employee


DATA_PATH = Path(__file__).parent / "employees.json"


with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

EMPLOYEES = [Employee(**emp) for emp in data["employees"]]
