"""Resource module."""

from functools import lru_cache

import boto3


class DynamoDBResource:
    """DynamoDB resource class."""

    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
        self.resource = boto3.resource(
            'dynamodb',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name,
        )

    def get_table(self, table_name):
        return self.resource.Table(table_name)

    def get_describe_table(self, table_name):
        return self.resource.Table(table_name).describe()


@lru_cache(maxsize=1)
def init_dynamodb_resource(
        aws_access_key_id: str, aws_secret_access_key: str, region_name: str,
) -> DynamoDBResource:
    return DynamoDBResource(
        aws_access_key_id,
        aws_secret_access_key,
        region_name,
    )
