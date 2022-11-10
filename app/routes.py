"""Routes module."""

from fastapi import APIRouter, Depends, HTTPException, status

from app.application import Application, init_application
from app.schemas import (CommentInSchema, CommentOutSchema, ThreadInSchema,
                         ThreadOutSchema)

router = APIRouter()


@router.get(
    '/threads',
    tags=['threads'],
    response_model=list[ThreadOutSchema],
)
def get_threads(
        thread_service: Application = Depends(init_application),
):
    """Get all threads."""
    return thread_service.thread_service.get_all()


@router.get(
    '/threads/{thread_id}',
    tags=['threads'],
    response_model=ThreadOutSchema,
)
def get_thread_by_id(
        thread_id: str,
        thread_service: Application = Depends(init_application),
):
    """Get thread by id."""
    try:
        thread = thread_service.thread_service.get_by_id(thread_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
    return thread


@router.post(
    '/threads',
    tags=['threads'],
    status_code=status.HTTP_201_CREATED,
    response_model=str,
)
def create_thread(
        thread: ThreadInSchema,
        thread_service: Application = Depends(init_application),
):
    """Create thread."""
    try:
        thread_id = thread_service.thread_service.create(
            user_id=thread.user_id,
            title=thread.title,
            description=thread.description,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    return thread_id


@router.put(
    '/threads/{thread_id}',
    tags=['threads'],
    response_model=ThreadOutSchema,
)
def update_thread(
        thread_id: str,
        thread_in: ThreadInSchema,
        thread_service: Application = Depends(init_application),
):
    """Update thread."""
    try:
        thread = thread_service.thread_service.get_by_id(thread_id)
        if thread is None:
            raise ValueError('Thread not found')

        if thread['user_id'] != thread_in.user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail='Forbidden',
            )

        response = thread_service.thread_service.update(
            thread_id=thread_id,
            title=thread_in.title,
            description=thread_in.description,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    return response


@router.put(
    'threads/{thread_id}/like',
    tags=['threads'],
)
def like_thread(
        thread_id: str,
        user_id: str,
        thread_service: Application = Depends(init_application),
):
    """Like thread."""
    try:
        thread = thread_service.thread_service.get_by_id(thread_id)
        if thread is None:
            raise ValueError('Thread not found')

        response = thread_service.thread_service.like(
            thread_id=thread_id,
            user_id=user_id,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    return response


@router.get(
    '/comments',
    tags=['comments'],
    response_model=list[CommentOutSchema],
)
def get_comments(
        comment_service: Application = Depends(init_application),
):
    return comment_service.comment_service.get_all()


@router.get(
    '/comments/{comment_id}',
    tags=['comments'],
    response_model=CommentOutSchema,
)
def get_comment_by_id(
        comment_id: str,
        comment_service: Application = Depends(init_application),
):

    try:
        comment = comment_service.comment_service.get_by_id(comment_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
    return comment


@router.post(
    '/comments',
    tags=['comments'],
    status_code=status.HTTP_201_CREATED,
    response_model=str,
)
def create_comment(
        comment: CommentInSchema,
        comment_service: Application = Depends(init_application),
):

    try:
        comment_id = comment_service.comment_service.create(
            thread_id=comment.thread_id,
            user_id=comment.user_id,
            comment=comment.comment,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    return comment_id


@router.delete(
    '/comments/{comment_id}',
    tags=['comments'],
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_comment(
        comment_id: str,
        comment_service: Application = Depends(init_application),
):
    """Delete comment."""
    try:
        comment_service.comment_service.delete(comment_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
