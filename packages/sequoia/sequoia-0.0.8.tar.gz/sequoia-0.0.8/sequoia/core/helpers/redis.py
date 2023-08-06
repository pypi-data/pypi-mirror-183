import aioredis

from sequoia.core.config import config


redis = aioredis.from_url(
    url=f"{config.REDIS.MAIN.URI}", encoding="utf-8", decode_responses=True)
