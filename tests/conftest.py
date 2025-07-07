import pytest
@pytest.fixture
def test_user():
    return {
        'name':'Alice',
        'username': 'alice123',
        'email': 'alice@example.com'
    }