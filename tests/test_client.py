import pytest
import respx
from httpx import Response
from tuulpy import TuulClient, AsyncTuulClient
from tuulpy.exceptions import AuthenticationError, PermissionError, RateLimitError

BASE_URL = "https://api.tuul.digitwhale.com"

@respx.mock
def test_generative_success():
    # Mock the API response
    respx.post(f"{BASE_URL}/generative").mock(
        return_value=Response(200, json={
            "id": "gen_123",
            "content": "Hello world",
            "usage": {"tokens": 10},
            "created_at": 1234567890
        })
    )

    client = TuulClient(api_key="test_key")
    resp = client.generative.create("Hi")
    
    assert resp.content == "Hello world"
    assert resp.id == "gen_123"

@respx.mock
def test_authentication_error_401():
    # Mock a 401 error
    respx.post(f"{BASE_URL}/generative").mock(
        return_value=Response(401, json={"error": {"message": "Invalid Key"}})
    )

    client = TuulClient(api_key="bad_key")
    
    with pytest.raises(AuthenticationError) as exc:
        client.generative.create("Hi")
    assert "Invalid Key" in str(exc.value)

@respx.mock
def test_ip_whitelist_error_403():
    # Mock a 403 error (IP whitelist issue)
    respx.post(f"{BASE_URL}/generative").mock(
        return_value=Response(403, json={"error": {"message": "Forbidden"}})
    )

    client = TuulClient(api_key="test_key")
    
    with pytest.raises(PermissionError) as exc:
        client.generative.create("Hi")
    
    # Ensure our custom exception message about IP whitelisting is present
    assert "IP is whitelisted" in str(exc.value)

@respx.mock
def test_retry_mechanism():
    # Mock a 500 followed by a 200 (Success)
    route = respx.post(f"{BASE_URL}/generative")
    route.side_effect = [
        Response(500),  # First attempt fails
        Response(200, json={
            "id": "gen_retry", "content": "Success", "usage": {}, "created_at": 1
        })
    ]

    client = TuulClient(api_key="test_key", max_retries=2)
    resp = client.generative.create("Retry test")
    
    assert resp.content == "Success"
    assert route.call_count == 2  # Proves it retried

@pytest.mark.asyncio
@respx.mock
async def test_async_conversation_flow():
    respx.post(f"{BASE_URL}/conversation").mock(
        return_value=Response(200, json={
            "session_id": "sess_001",
            "message": {"role": "agent", "content": "I can help"},
            "metadata": {}
        })
    )

    async with AsyncTuulClient(api_key="test_key") as client:
        resp = await client.conversation.send("Help me")
        assert resp.session_id == "sess_001"
        assert resp.message.content == "I can help"