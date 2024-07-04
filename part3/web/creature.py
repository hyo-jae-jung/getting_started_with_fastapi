from fastapi import APIRouter
import sys
sys.path.append("/mnt/d/hyojaejung/workspace/Mywork/getting_started_with_fastapi/part3")
from model.creature import Creature 
import fake.creature as service 

router = APIRouter(prefix="/creature")

@router.get("/")
def get_all() -> list[Creature]:
    return service.get_all()


@router.get("/{name}")
def get_one(name) -> Creature:
    return service.get_one(name)


@router.post("/")
def create(creature: Creature) -> Creature:
    return service.create(creature)

@router.patch("/{name}")
def modify(name, creature: Creature) -> Creature:
    return service.create(name, creature)

@router.put("/{name}")
def replace(name, creature: Creature) -> Creature:
    return service.create(name, creature)

@router.delete("/{name}")
def delete(name: str):
    return service.delete(name)