from fastapi import APIRouter, Depends, HTTPException
from aioredis import Redis, from_url
from pydantic import BaseModel, Field
from typing import Dict, AsyncGenerator

router = APIRouter(prefix="/dummy")

class Item(BaseModel):
    """Represents an item with a key and a value for storing in Redis."""
    key: str = Field(..., description="The key of the item")
    value: Dict[str, str] = Field(..., description="The value of the item, a dictionary of strings")

async def get_redis_cache() -> AsyncGenerator[Redis, None]:
    """
    Dependency that provides a Redis connection.
    Automatically closes the connection when the request is finished.
    """
    redis = await from_url("redis://localhost:6379")
    try:
        yield redis
    finally:
        await redis.close()

@router.post("/populate/", summary="Populate Redis", response_description="The item stored in Redis")
async def populate_redis(
    item: Item,
    cache: Redis = Depends(get_redis_cache)
) -> dict:
    """
    Stores an item in Redis using a key-value pair.

    Args:
        item: An instance of Item, containing the key and value to store.
        cache: Redis connection instance.

    Returns:
        A dictionary with a message, key, and value of the stored item.
    """
    if not item.key or not item.value:
        raise HTTPException(status_code=400, detail="Key and value must be provided.")
    await cache.set(item.key, item.value.json())  # Pydantic's .json() method for serialization
    return {"message": "Data successfully saved to Redis", "key": item.key, "value": item.value}

@router.get("/retrieve/", summary="Retrieve from Redis", response_model=Item, response_description="The retrieved item")
async def retrieve_redis(
    key: str,
    cache: Redis = Depends(get_redis_cache)
) -> Item:
    """
    Retrieves an item from Redis by key.

    Args:
        key: The key of the item to retrieve.
        cache: Redis connection instance.

    Returns:
        An instance of Item containing the key and the retrieved value.

    Raises:
        HTTPException: If the item is not found or if there's an issue decoding the JSON data.
    """
    result = await cache.get(key)
    if result is None:
        raise HTTPException(status_code=404, detail="Item not found")

    # Decode result from bytes to string if necessary, handle JSON decoding safely
    try:
        value_dict = json.loads(result.decode("utf-8") if isinstance(result, bytes) else result)
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding JSON data from Redis")

    return Item(key=key, value=value_dict)
