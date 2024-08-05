from typing import Annotated

from fastapi import APIRouter, Path


router = APIRouter(prefix='/items', tags=['Items'])



@router.get("/")
def list_items():
    return {
        "item1",
        'item2',
    }
@router.get("/laters/")
def get_latest_items():
    return {"items": {"id": "0", "name": 'Laters'}}

@router.get("/{item_id}")
def get_item_by_id(item_id: Annotated[int, Path(ge = 1, lt = 1_000_000)]):
    return{
        "items" : {
            "id": item_id,
        }
    }