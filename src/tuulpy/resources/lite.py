from ..types.lite import LiteRequest, LiteResponse

class LiteResource:
    def __init__(self, client):
        self._client = client

    def generate(self, prompt: str, model: str = "tuul-lite-v1") -> LiteResponse:
        """
        Low-latency generation for real-time applications.
        """
        payload = LiteRequest(prompt=prompt, model=model).model_dump()
        data = self._client.post("/lite/generate", json=payload)
        return LiteResponse(**data)

class AsyncLiteResource:
    def __init__(self, client):
        self._client = client

    async def generate(self, prompt: str, model: str = "tuul-lite-v1") -> LiteResponse:
        payload = LiteRequest(prompt=prompt, model=model).model_dump()
        data = await self._client.post("/lite/generate", json=payload)
        return LiteResponse(**data)