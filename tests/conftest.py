"""Conftest file."""

import boto3
import pytest
from moto.dynamodb import mock_dynamodb

from app.repositories import CommentRepository, ThreadRepository


@pytest.fixture
def dynamodb_connect():
    @mock_dynamodb
    def dynamodb_client():
        dynamodb = boto3.resource('dynamodb', region_name='eu-west-2')

        # Create the table
        dynamodb.create_table(
            TableName=ThreadRepository.TABLE_NAME,
            KeySchema=[
                {
                    'AttributeName': 'thread_id',
                    'KeyType': 'HASH',
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'thread_id',
                    'AttributeType': 'S',
                },
            ],
            # BillingMode='PROVISIONED',
            ProvisionedThroughput={
                'ReadCapacityUnits': 40,
                'WriteCapacityUnits': 40,
            },

        )
        dynamodb.create_table(
            TableName=CommentRepository.TABLE_NAME,
            KeySchema=[
                {
                    'AttributeName': 'comment_id',
                    'KeyType': 'HASH',
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'comment_id',
                    'AttributeType': 'S',
                },
            ],
            # BillingMode='PROVISIONED',
            ProvisionedThroughput={
                'ReadCapacityUnits': 40,
                'WriteCapacityUnits': 40,
            },
        )
        return dynamodb

    return dynamodb_client


@pytest.fixture
def dynamodb_resource_fake():
    class DynamoDBResourceFake:
        def __init__(self, resource):
            self.resource = resource

        def get_table(self, table_name):
            return self.resource.Table(table_name)

    return DynamoDBResourceFake
