"""Test repository."""

from moto.dynamodb import mock_dynamodb

from app.repositories import ThreadRepository


@mock_dynamodb
def test_thread_get_by_id(dynamodb_connect, dynamodb_resource_fake):
    repository = ThreadRepository(dynamodb_resource_fake(dynamodb_connect()))
    result = repository.get_by_id('test')
    assert result is None

    thread_id = repository.create('test', 'test', 'test')

    result = repository.get_by_id(thread_id)

    assert result is not None
