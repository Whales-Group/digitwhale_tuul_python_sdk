from pydantic import BaseModel, Field
from typing import Optional, List, Union, Dict, Any

# Helper for file/image input
class ImageOptions(BaseModel):
    file: Union[str, bytes] 
    filename: str
    mediaType: Optional[str] = None
    type: str # "file" or "image"
    url: Optional[str] = None


# Nested Models
class PromptOptions(BaseModel):
    prompt: str
    files: Optional[List[ImageOptions]] = None

class AgentOptions(BaseModel):
    agentId: str
    agentVersion: Optional[str] = None

class SessionOptions(BaseModel):
    sessionId: str
    conversationId: Optional[str] = None

class StateOptions(BaseModel):
    newConversation: Optional[bool] = None
    cancelGeneration: bool = False

class AbilityOptions(BaseModel):
    reasoning: bool
    webSearch: bool

    
# Primary Payload Model
class OpenaiPayload(BaseModel):
    promptOptions: PromptOptions
    stateOptions: StateOptions
    sessionOptions: SessionOptions
    agentOptions: AgentOptions
    abilityOptions: AbilityOptions







class GenVersion(BaseModel):
    id: str
    content: str


class GenResponseItem(BaseModel):
    from_: str = Field(..., alias="from")
    versions: List[GenVersion]

    tools: Optional[Any] = None
    id: str
    createdAt: str
    updatedAt: str


class GenStats(BaseModel):
    messages: int
    functionsCalled: int
    avgResponse: float
    errors: int


class GenMetaData(BaseModel):
    session_id: str
    agentId: str
    agentVersion: Optional[str] = None
    stats: GenStats
    error_logs: List[Any]


class GenData(BaseModel):
    response: GenResponseItem
    meta_data: GenMetaData


class GenerateResponse(BaseModel):
    status: bool
    statusCode: int
    message: str
    data: GenData
    error: Optional[Any] = None

