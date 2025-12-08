from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any


class ConversationRequest(BaseModel):
    session_id: str

class HistoryVersion(BaseModel):
    id: str
    content: str


class HistoryItem(BaseModel):
    id: str
    key: str
    from_: str = Field(..., alias="from")
    versions: List[HistoryVersion]

    tools: Optional[Any] = None
    sources: Optional[Any] = None
    reasoning: Optional[Any] = None
    chainOfThought: Optional[Any] = None
    plan: Optional[Any] = None
    contextData: Optional[Any] = None
    confirmation: Optional[Any] = None
    checkpoints: Optional[Any] = None
    suggestions: Optional[Any] = None
    tasks: Optional[Any] = None
    messageQueue: Optional[Any] = None

    conversationId: str
    session_id: str
    createdAt: str
    updatedAt: str


class MetaData(BaseModel):
    session_id: str
    agent_id: str
    api_key_used: bool


class HistoryData(BaseModel):
    count: int
    history: List[HistoryItem]
    meta_data: MetaData


class HistoryResponse(BaseModel):
    status: bool
    statusCode: int
    message: str
    data: HistoryData
    error: Optional[Any] = None



