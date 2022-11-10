"""Application module."""

from functools import lru_cache

from app.config import Config
from app.repositories import CommentRepository, ThreadRepository
from app.resources import init_dynamodb_resource
from app.services import CommentService, ThreadService


class Application(object):
    """."""

    def __init__(self):
        self.config = Config()
        self.dynamodb_resource = init_dynamodb_resource(
            aws_access_key_id=self.config.aws_access_key_id,
            aws_secret_access_key=self.config.aws_secret_access_key,
            region_name=self.config.region_name,
        )
        self.thread_repository = ThreadRepository(self.dynamodb_resource)
        self.comment_repository = CommentRepository(self.dynamodb_resource)
        self.thread_service: ThreadService = ThreadService(
            self.thread_repository,
        )
        self.comment_service: CommentService = CommentService(
            comment_repository=self.comment_repository,
            thread_repository=self.thread_repository,
        )


@lru_cache(maxsize=1)
def init_application() -> Application:
    return Application()
