from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy.future import select
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.centro_treinamento.schemas import *
from workout_api.contrib.repository.dependencies import DatabaseDependency

router = APIRouter()


@router.post(
    path="/",
    summary="Criar criar novo Centro de Treinamento",
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoOut,
)
async def post(
    db_session: DatabaseDependency, centro_treinamento_in: CentroTreinamentoIn = Body(...)
) -> CentroTreinamentoOut:

    centro_treinamento_model = CentroTreinamentoModel(**centro_treinamento_in.model_dump())
    db_session.add(centro_treinamento_model)
    await db_session.commit()
    await db_session.refresh(centro_treinamento_model)

    return centro_treinamento_model


@router.get(
    path="/",
    summary="Consultar todos os centros",
    status_code=status.HTTP_200_OK,
    response_model=list[CentroTreinamentoOut],
)
async def query(db_session: DatabaseDependency) -> list[CentroTreinamentoOut]:
    centros: list[CentroTreinamentoOut] = (await db_session.execute(select(CentroTreinamentoModel))).scalars().all()

    return centros


@router.get(
    path="/{id}",
    summary="Consultar centro pelo id",
    status_code=status.HTTP_200_OK,
    response_model=CentroTreinamentoOut,
)
async def query(id: UUID4, db_session: DatabaseDependency) -> CentroTreinamentoOut:
    centro: CentroTreinamentoOut = (
        (await db_session.execute(select(CentroTreinamentoModel).where(CentroTreinamentoModel.id == id)))
        .scalars()
        .first()
    )

    if not centro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Centro não encontrada para o id {id}")

    return centro
