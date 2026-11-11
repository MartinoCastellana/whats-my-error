# FastAPI example (illustrative)

Check existing exception handlers and OpenAPI response schemas before proposing changes. Do not replace validation handling or alter status codes silently.

```python
from fastapi import HTTPException

async def load_profile(client, url):
    try:
        response = await client.get(url, timeout=5.0)
        response.raise_for_status()
        return response.json()
    except TimeoutError as exc:
        # Map to the documented timeout contract at the API boundary.
        raise HTTPException(status_code=504, detail="Upstream request timed out") from exc
```

The detail shown is illustrative. Confirm public wording and upstream status mapping from the actual API contract.
