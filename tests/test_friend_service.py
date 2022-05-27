from app.src.service.friend_service import Friend


def test_friend():
    response = Friend
    assert response is not None


def test_table_name():
    assert Friend.__tablename__ == 'friend'


def test_table_fields():
    assert Friend.__table__.columns['id'] is not None
    assert Friend.__table__.columns['first_name'] is not None
    assert Friend.__table__.columns['last_name'] is not None
    assert Friend.__table__.columns['age'] is not None


def test_constructor():
    friend = Friend(
        first_name='John',
        last_name='Doe',
        age=20
    )
    
    assert friend.first_name == 'John'
    assert friend.last_name == 'Doe'
    assert friend.age == 20

