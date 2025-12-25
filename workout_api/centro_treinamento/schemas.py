from typing import Annotated

from pydantic import UUID4, Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description="Nome do CT", example="CT Kings", max_length=20)]
    endereco: Annotated[str, Field(description="Endereço do CT", example="Rua X, 50", max_length=60)]
    proprietario: Annotated[str, Field(description="Proprietário do CT", example="CT Kings", max_length=30)]


class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description="Identificador do centro de treinamento")]


class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do Centro de treinamento", example="CT Kings", max_length=20)]
