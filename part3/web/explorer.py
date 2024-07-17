from fastapi import APIRouter 
import sys
sys.path.append("/mnt/d/hyojaejung/workspace/Mywork/getting_started_with_fastapi/part3")
from model.explorer import Explorer
# import fake.explorer as service
import service.explorer as service

router = APIRouter(prefix="/explorer")

@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()

@router.get("/{name}")
def get_one(name) -> Explorer | None:
    return service.get_one(name)

@router.post("/")
def create(name, explorer: Explorer) -> Explorer:
    return service.create(name, explorer)

@router.patch("/{name}")
def modify(name, explorer: Explorer) -> Explorer:
    return service.modify(name, explorer)

@router.put("/{name}")
def replace(name, explorer: Explorer) -> Explorer:
    return service.replace(name, explorer)

@router.delete("/{name}")
def delete(name: str):
    return service.delete(name)
