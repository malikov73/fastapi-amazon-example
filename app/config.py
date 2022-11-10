"""Config module."""

from pydantic import BaseSettings


class Config(BaseSettings):
    """Config class."""

    aws_access_key_id: str
    aws_secret_access_key: str
    region_name: str
