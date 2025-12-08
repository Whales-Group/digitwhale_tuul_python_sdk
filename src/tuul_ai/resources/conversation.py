from typing import Optional, List
from ..types.conversation import (
    ConversationRequest,
    HistoryResponse
)

class ConversationResource:
    def __init__(self, client):
        self._client = client

    def send(self, message: str, session_id: Optional[str] = None, **kwargs) -> HistoryResponse:
        """
        Send a message to a conversation agent.
        """
        payload = ConversationRequest(
            message=message, 
            session_id=session_id, 
            **kwargs
        ).model_dump(exclude_none=True)
        
        data = self._client.post("/conversation", json=payload)
        return HistoryResponse(**data)

    def history(self, session_id: str) -> HistoryResponse:
        """
        Retrieve message history for a specific session.
        """
        # GET request handling needs to be added to BaseClient or called directly via _client
        # Assuming we add a simple .get helper in BaseClient similar to .post
        data = self._client.get(f"/conversation/{session_id}/history")
        return HistoryResponse(**data)


class AsyncConversationResource:
    def __init__(self, client):
        self._client = client

    async def send(self, message: str, session_id: Optional[str] = None, **kwargs) -> HistoryResponse:
        payload = ConversationRequest(
            message=message, 
            session_id=session_id, 
            **kwargs
        ).model_dump(exclude_none=True)
        
        data = await self._client.post("/conversation", json=payload)
        return HistoryResponse(**data)

    async def history(self, session_id: str) -> HistoryResponse:
        data = await self._client.get(f"/conversation/{session_id}/history")
        return HistoryResponse(**data)