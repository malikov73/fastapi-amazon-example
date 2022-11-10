"""Schemas for the API."""

from pydantic import BaseModel


class ThreadInSchema(BaseModel):
    title: str
    description: str
    user_id: str


class ThreadOutSchema(BaseModel):
    thread_id: str
    title: str
    description: str
    user_id: str
    likes: list[str]
    created_at: str


class CommentInSchema(BaseModel):
    thread_id: str
    user_id: str
    comment: str


class CommentOutSchema(BaseModel):
    comment_id: str
    thread_id: str
    user_id: str
    comment: str
    created_at: str
