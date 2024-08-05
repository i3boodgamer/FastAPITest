from . import crud
from .schemas import Product, ProductCreate, ProductUpdate, ProductPartial
from .dependencies import product_by_id

from core.models import db_helper

from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(tags = ["Products"])


@router.get("/", response_model = list[Product])
async def get_products(session: AsyncSession = Depends(db_helper.session_despendency)):
    return await crud.get_products(session = session)

@router.post("/", response_model = Product)
async def create_product(product: ProductCreate, session: AsyncSession = Depends(db_helper.session_despendency)):
    return await crud.create_product(session = session, product_in = product)

@router.get("/{product_id}/", response_model = Product)
async def get_product(product_id: Product = Depends(product_by_id)):
    return product_id

@router.put("/{product_id}/")
async def update_product(product_update: ProductUpdate, product: Product = Depends(product_by_id), session: AsyncSession = Depends(db_helper.session_despendency)):
    return await crud.update_product(
        session = session,
        product = product,
        product_update = product_update,
    )

@router.patch("/{product_id}/")
async def update_product(product_update: ProductPartial, product: Product = Depends(product_by_id), session: AsyncSession = Depends(db_helper.session_despendency)):
    return await crud.update_product(
        session = session,
        product = product,
        product_update = product_update,
        partial = True
    )
    
@router.delete("/{product_id}/", status_code = status.HTTP_204_NO_CONTENT)
async def delete_product(product: Product = Depends(product_by_id), session: AsyncSession = Depends(db_helper.session_despendency)) -> None:
    return await crud.delete_product(session = session, product = product)