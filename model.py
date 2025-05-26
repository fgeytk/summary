from pydantic import BaseModel
from typing import Literal, Optional

class SummarizationRequest(BaseModel):
    text: str
    mode: Optional[Literal["short", "detailed", "bullet"]] = "short"