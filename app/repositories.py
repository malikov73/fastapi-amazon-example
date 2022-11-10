"""Repository module."""

from datetime import datetime
from typing import Optional
from uuid import uuid4


class ThreadRepository(object):
    """Thread repository."""

    TABLE_NAME = 'Thread'

    def __init__(self, dynamodb_resource):
        self.table = dynamodb_resource.get_table(self.TABLE_NAME)

    def get_by_id(self, thread_id: str) -> Optional[dict]:
        response = self.table.get_item(
            Key={
                'thread_id': thread_id,
            },
        )
        if 'Item' in response:
            return response['Item']
        return None

    def create(
            self, user_id: str,
            title: str, description: str,
    ) -> Optional[str]:
        thread_id = uuid4().hex
        response = self.table.put_item(
            Item={
                'thread_id': thread_id,
                'user_id': user_id,
                'title': title,
                'description': description,
                'likes': [],
                'created_at': datetime.now().isoformat(),

            },
        )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return thread_id
        return None

    def update(
            self, thread_id: str, title: str, description: str,
            likes: list[str],
    ) -> None:
        response = self.table.update_item(
            Key={
                'thread_id': thread_id,
            },
            UpdateExpression='SET title = :title, description = '
                             ':description, likes = :likes',
            ExpressionAttributeValues={
                ':title': title,
                ':description': description,
                ':likes': likes,
            },
        )
        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            raise ValueError('Thread not updated')

    def get_all(self) -> list[dict]:
        response = self.table.scan()
        data = response['Items']
        while 'LastEvaluatedKey' in response and len(data):
            response = self.table.scan(
                ExclusiveStartKey=response['LastEvaluatedKey'],
            )
            data.extend(response['Items'])

        return data


class CommentRepository(object):
    """Comment repository."""

    TABLE_NAME = 'Comment'

    def __init__(self, dynamodb_resource):
        self.table = dynamodb_resource.get_table(self.TABLE_NAME)

    def get_by_id(self, comment_id: str) -> Optional[dict]:
        response = self.table.get_item(
            Key={
                'comment_id': comment_id,
            },
        )
        if 'Item' in response:
            return response['Item']
        return None

    def create(
            self, user_id: str,
            thread_id: str, comment: str,
    ) -> Optional[str]:
        comment_id = uuid4().hex
        response = self.table.put_item(
            Item={
                'comment_id': comment_id,
                'user_id': user_id,
                'thread_id': thread_id,
                'comment': comment,
                'created_at': datetime.now().isoformat(),
            },
        )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return comment_id
        return None

    def delete(self, comment_id: str) -> None:
        response = self.table.delete_item(
            Key={
                'comment_id': comment_id,
            },
        )
        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            raise ValueError('Failed to delete comment')

    def get_all(self) -> list[dict]:
        response = self.table.scan()
        data = response['Items']
        while 'LastEvaluatedKey' in response and len(data):
            response = self.table.scan(
                ExclusiveStartKey=response['LastEvaluatedKey'],
            )
            data.extend(response['Items'])
        return data
