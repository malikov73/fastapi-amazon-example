"""Forum services module."""
from app.repositories import CommentRepository, ThreadRepository


class ThreadService(object):
    """Thread service."""

    def __init__(self, forum_repository: ThreadRepository):
        self.thread_repository: ThreadRepository = forum_repository

    def get_by_id(self, thread_id: str) -> dict:
        result = self.thread_repository.get_by_id(thread_id)
        if result is None:
            raise ValueError('Thread not found')
        return result

    def get_all(self) -> list[dict]:
        return self.thread_repository.get_all()

    def create(self, user_id: str, title: str, description: str) -> str:
        thread_id = self.thread_repository.create(user_id, title, description)
        if thread_id is None:
            raise ValueError('Thread not created')
        return thread_id

    def update(
            self, thread_id: str, title: str, description: str,
    ) -> dict:

        thread = self.thread_repository.get_by_id(thread_id)
        if thread is None:
            raise ValueError('Thread not found')

        likes = thread['likes']
        self.thread_repository.update(
            thread_id, title, description, likes,
        )
        thread = self.thread_repository.get_by_id(thread_id)
        return thread

    def like(self, thread_id: str, user_id: str) -> dict:
        thread = self.thread_repository.get_by_id(thread_id)
        if thread is None:
            raise ValueError('Thread not found')

        likes = thread['likes']
        if user_id not in likes:
            likes.append(user_id)
        else:
            likes.remove(user_id)

        self.thread_repository.update(
            thread_id, thread['title'], thread['description'], likes,
        )
        thread = self.thread_repository.get_by_id(thread_id)
        return thread


class CommentService(object):
    """Comment service."""

    def __init__(
            self, comment_repository: CommentRepository,
            thread_repository: ThreadRepository,
    ):
        self.comment_repository: CommentRepository = comment_repository
        self.thread_repository: ThreadRepository = thread_repository

    def get_by_id(self, comment_id: str) -> dict:
        result = self.comment_repository.get_by_id(comment_id)
        if result is None:
            raise ValueError('Comment not found')
        return result

    def get_all(self) -> list[dict]:
        return self.comment_repository.get_all()

    def create(
            self, thread_id: str, user_id: str,
            comment: str,
    ) -> str:
        thread = self.thread_repository.get_by_id(thread_id)
        if thread is None:
            raise ValueError('Thread not found')
        comment_id = self.comment_repository.create(
            thread_id, user_id, comment,
        )
        if comment_id is None:
            raise ValueError('Comment not created')
        return comment_id

    def delete(self, comment_id: str) -> None:
        self.comment_repository.delete(comment_id)
