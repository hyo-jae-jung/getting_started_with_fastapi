import sys
sys.path.append('/mnt/d/hyojaejung/workspace/Mywork/getting_started_with_fastapi/part3')
from model.explorer import Explorer 
import fake.explorer as data 
from typing import List

def get_all() -> List[Explorer]:
    return data.get_all()

def get_one(name: str) -> Explorer | None:
    return data.get_one(name)

def create(explorer: Explorer) -> Explorer:
    return data.create(explorer)

def replace(name: str, explorer: Explorer) -> Explorer:
    return data.replace(name, explorer)

def modify(name: str, explorer: Explorer) -> Explorer:
    return data.modify(name, explorer)

def delete(name: str) -> bool:
    return data.delete(name)
