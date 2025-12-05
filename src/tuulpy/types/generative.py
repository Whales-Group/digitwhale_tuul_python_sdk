from pydantic import BaseModel, Field
from typing import Optional, List

class GenerateRequest(BaseModel):
    prompt: str
    model: Optional[str] = "tuul-gen-v1"
    max_tokens: int = Field(default=1024, ge=1)
    temperature: float = 0.7

class GenerateResponse(BaseModel):
    id: str
    content: str
    usage: dict
    created_at: int