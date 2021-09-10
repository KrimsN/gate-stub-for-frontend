import typing as t

from pydantic import BaseModel, Field
from enum import Enum


class WSTargetType(str, Enum):
    telegram = 'telegram'
    instagram = 'instagram'


class AddTaskByTagBodyScheme(BaseModel):
    tag: str
    target: WSTargetType
    method: str  # TODO: Сделать норм валидацию
    data: dict


class AddTaskByWsIdsBodyScheme(BaseModel):
    wsids: list[str]
    target: WSTargetType
    method: str
    data: dict


class AddTaskByUsernameScheme(BaseModel):
    username: str
    target: WSTargetType
    method: str
    data: dict
