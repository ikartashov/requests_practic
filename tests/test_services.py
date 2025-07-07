from app.services import get_user, create_user, update_user

def test_created_user(test_user):
    result = create_user(test_user)
    assert result is not None
    assert result['username'] == 'alice123'
    assert result['name'] == 'Alice'
    assert result['email'] == 'alice@example.com'

def test_update_user(test_user):
    result = update_user(user_id=1, data=test_user)
    assert result is not None

def test_get_user():
    user = get_user(1)
    assert user is not None
    assert user['id'] == 1

def test_get_user_not_found():
    user = get_user(9999)
    assert user is None