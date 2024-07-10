import sys
sys.path.append('/mnt/d/hyojaejung/workspace/Mywork/getting_started_with_fastapi/part3')
from model.creature import Creature 
import fake.creature as data 
from typing import List

def get_all() -> List[Creature]:
    return data.get_all()

def get_one(name: str) -> Creature | None:
    return data.get_one(name)

def create(creature: Creature) -> Creature:
    return data.create(creature)

def replace(name: str, creature: Creature) -> Creature:
    return data.replace(name, creature)

def modify(name: str, creature: Creature) -> Creature:
    return data.modify(name, creature)

def delete(name: str) -> bool:
    return data.delete(name)
