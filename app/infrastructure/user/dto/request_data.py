from enum import StrEnum

from pydantic import BaseModel, Field


class NicType(StrEnum):
    universal = 'universal'
    local = 'local'


class Nic(BaseModel):
    uuid: str | None
    num: str
    type: NicType = Field(description='value should be in (universal, local)}')


class UserModel(BaseModel):
    uuid: str | None
    name: str
    lastname: str
    email: str
    password: str
    age: int
    nif_stat: int | str = Field(alias='nifStat', ge=3, le=5)
