from pydantic import BaseModel
from typing import Optional

class LiteRequest(BaseModel):
    prompt: str
    model: str = "tuul-lite-v1"

class LiteResponse(BaseModel):
    content: str
    latency_ms: float