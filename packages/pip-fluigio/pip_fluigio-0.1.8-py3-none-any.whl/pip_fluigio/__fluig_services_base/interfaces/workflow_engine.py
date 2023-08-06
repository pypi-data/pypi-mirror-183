from typing import List, Optional
from pydantic import BaseModel, Field


class Attachments(BaseModel):
    attach: str
    editing: str
    file_name: str
    file_size: str
    file_content: str
    principal: str


class Colleagues(BaseModel):
    item: str


class Item(BaseModel):
    key: str
    value: str


class CardData(BaseModel):
    item: List[Item] = Field(default_factory=list)


class SaveAndSendTaskClassic(BaseModel):
    description: str
    process_instance_id: str
    choosed_state: str
    colleague_ids: List[Colleagues] = Field(default_factory=list)
    complete_task: str
    user_id: str
    colleague_name: str
    comments: Optional[str] = ""
    attachments: List[Attachments] = Field(default_factory=list)
    card_data: CardData
    appointment: Optional[str] = ""
    manager_mode: str
    thread_sequence: str
