from ..types.generative import GenerateRequest, GenerateResponse
from typing import Union, Dict, Any

class GenerativeResource:
    def __init__(self, client):
        self._client = client

    def create(self, prompt: str, **kwargs) -> GenerateResponse:
        """
        Generate text based on a prompt.
        Accepts specific args or a raw dictionary for future-proofing.
        """
        payload = GenerateRequest(prompt=prompt, **kwargs).model_dump(exclude_none=True)
        data = self._client.post("/generative", json=payload)
        return GenerateResponse(**data)

class AsyncGenerativeResource:
    def __init__(self, client):
        self._client = client

    async def create(self, prompt: str, **kwargs) -> GenerateResponse:
        payload = GenerateRequest(prompt=prompt, **kwargs).model_dump(exclude_none=True)
        data = await self._client.post("/generative", json=payload)
        return GenerateResponse(**data)