# tuulpy

The official Python SDK for Tuul.

## Features
- **Typed**: Full Pydantic models for Requests/Responses.
- **Async & Sync**: Native support for both `await` and standard blocking calls.
- **Robust**: Automatic retries with exponential backoff and IP-whitelist aware error handling.

## Installation
```bash
pip install tuulpy
````

## Quick Start

```python
import os
from tuulpy import TuulClient

client = TuulClient(api_key=os.getenv("TUUL_API_KEY"))

try:
    response = client.generative.create(prompt="Explain quantum physics")
    print(response.content)
except PermissionError:
    print("Please check your IP Whitelist settings in Tuul.")
```

## CLI Usage

```bash
export TUUL_API_KEY="your-key"
tuul generate "Hello world"
```
