"""Test thread service."""

from unittest import mock
from uuid import uuid4

import pytest

from app.repositories import ThreadRepository
from app.services import ThreadService


def test_thread_service_get_by_id():
    fake_thread_repository = mock.Mock(spec=ThreadRepository)
    thread_id = uuid4().hex
    fake_thread_repository.get_by_id.return_value = {
        'thread_id': thread_id,
        'title': 'test',
        'description': 'test',
    }
    thread_service = ThreadService(fake_thread_repository)

    assert thread_service.get_by_id(thread_id) is not None

    fake_thread_repository.get_by_id.return_value = None

    with pytest.raises(ValueError):
        thread_service.get_by_id(thread_id)


def test_thread_service_create():
    fake_thread_repository = mock.Mock(spec=ThreadRepository)
    thread_id = uuid4().hex
    fake_thread_repository.create.return_value = thread_id
    thread_service = ThreadService(fake_thread_repository)

    assert thread_service.create('test', 'test', 'test') == thread_id
