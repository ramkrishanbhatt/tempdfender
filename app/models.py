from pydantic import BaseModel
from typing import List

class UpdateDecisionModel(BaseModel):
    video_id: str
    status: str
    classes: List[str]
