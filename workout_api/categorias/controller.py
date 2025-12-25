from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy.future import select
from workout_api.categorias.models import CategoriaModel
from workout_api.categorias.schemas import CategoriaIn, CategoriaOut
from workout_api.contrib.repository.dependencies import DatabaseDependency

router = APIRouter()


@router.post(path="/", summary="Criar nova Categoria", status_code=status.HTTP_201_CREATED, response_model=CategoriaOut)
async def post(db_session: DatabaseDependency, categoria_in: CategoriaIn = Body(...)) -> CategoriaOut:

    categoria_model = CategoriaModel(**categoria_in.model_dump())
    db_session.add(categoria_model)
    await db_session.commit()
    await db_session.refresh(categoria_model)

    return categoria_model


@router.get(
    path="/", summary="Consultar todas as categorias", status_code=status.HTTP_200_OK, response_model=list[CategoriaOut]
)
async def query(db_session: DatabaseDependency) -> list[CategoriaOut]:
    categorias: list[CategoriaOut] = (await db_session.execute(select(CategoriaModel))).scalars().all()

    return categorias


@router.get(
    path="/{id}", summary="Consultar categoria pelo id", status_code=status.HTTP_200_OK, response_model=CategoriaOut
)
async def query(id: UUID4, db_session: DatabaseDependency) -> CategoriaOut:
    categoria: CategoriaOut = (
        (await db_session.execute(select(CategoriaModel).where(CategoriaModel.id == id))).scalars().first()
    )

    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Categoria não encontrada para o id {id}")

    return categoria
