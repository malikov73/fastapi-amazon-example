"""Resource module."""

from functools import lru_cache

import boto3


class DynamoDBResource:
    """DynamoDB resource class."""

    def __init__(self):
        self.resource = boto3.resource(
            'dynamodb'
        )

    def get_table(self, table_name):
        return self.resource.Table(table_name)

    def get_describe_table(self, table_name):
        return self.resource.Table(table_name).describe()


@lru_cache(maxsize=1)
def init_dynamodb_resource(
) -> DynamoDBResource:
    return DynamoDBResource()
