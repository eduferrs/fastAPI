from typing import Annotated, Optional

from pydantic import Field, PositiveFloat
from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta
from workout_api.contrib.schemas import BaseSchema, OutMixin


class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do atleta", example="João", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta", example="12345678900", max_length=11)]
    idade: Annotated[int, Field(description="Idade do atleta", example=18)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", example=80.5)]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta", example=1.75)]
    sexo: Annotated[str, Field(description="Sexo do atleta", example="M")]
    categoria: Annotated[CategoriaIn, Field(description="Categoria do atleta")]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description="CT do atleta")]


class AtletaIn(Atleta):
    pass


class AtletaOut(Atleta, OutMixin):
    pass


class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description="Nome do atleta", example="João", max_length=50)]
    idade: Annotated[Optional[int], Field(None, description="Idade do atleta", example=18)]


class AtletaBasicOut(BaseSchema, OutMixin):
    """
    Schema simplificado para o get all.
    Feito para exibir apenas esses 3 campos no resultado.
    """

    nome: Annotated[str, Field(description="Nome do atleta", example="João", max_length=50)]
    categoria: Annotated[CategoriaIn, Field(description="Categoria do atleta")]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description="CT do atleta")]
