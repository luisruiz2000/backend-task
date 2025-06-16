from pydantic import BaseModel
from typing import Optional

class CreateTaskModel(BaseModel):
    title: str
    description: Optional[str] = None
