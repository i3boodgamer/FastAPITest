from . import crud

from fastapi import Depends, Path, HTTPException, status

from typing import Annotated

from core.models import db_helper, Product

from sqlalchemy.ext.asyncio import AsyncSession

async def product_by_id(product_id: Annotated[int, Path], session: AsyncSession = Depends(db_helper.session_despendency)) -> Product:
    product =  await crud.get_product(session=session, product_id=product_id)
    if product is not None:
        return product

    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = f"Product {product_id} not found!",
    )