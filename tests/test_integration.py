import pytest
import os
from tuulpy import TuulClient, AsyncTuulClient
from tuulpy.exceptions import AuthenticationError

# Skip if no key provided
pytestmark = pytest.mark.skipif(
    not os.getenv("TUUL_API_KEY"), 
    reason="TUUL_API_KEY not set"
)

def test_sync_generative_flow():
    client = TuulClient(api_key=os.environ["TUUL_API_KEY"])
    response = client.generative.create(prompt="Say hello")
    assert response.content is not None
    assert response.id is not None

@pytest.mark.asyncio
async def test_async_generative_flow():
    async with AsyncTuulClient(api_key=os.environ["TUUL_API_KEY"]) as client:
        response = await client.generative.create(prompt="Say hello async")
        assert response.content is not None