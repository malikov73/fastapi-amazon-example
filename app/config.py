"""Config module."""

from pydantic import BaseSettings


class Config(BaseSettings):
    """Config class."""

    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_DEFAULT_REGION: str
