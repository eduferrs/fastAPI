from typing import Annotated

from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description="Nome do CT", example="CT Kings", max_length=20)]
    endereco: Annotated[str, Field(description="Endereço do CT", example="Rua X, 50", max_length=60)]
    proprietario: Annotated[str, Field(description="Proprietário do CT", example="CT Kings", max_length=30)]
