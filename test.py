from unittest.mock import patch, MagicMock

import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

mock_user_data = {
    "name": "Vishwanath",
    "username": "vish2kber",
    "email": "vish2kber@gmail.com",
    "address": {
        "street": "Berlin",
        "suite": "Suite 222",
        "city": "Berlin111",
        "zipcode": "111111",
        "geo": {
            "lat": "-22.922",
            "lng": "-44.666"
        }
    },
    "phone": "9611941257",
    "website": "no_website_yet.net",
    "company": {
        "name": "Turbit",
        "catchPhrase": "Waiting to get into company",
        "bs": "Lets go!!"
    }
}


@pytest.fixture
def mock_db():
    with patch("crud.user_db") as mock_user_db, \
            patch("crud.post_db") as mock_post_db, \
            patch("crud.comment_db") as mock_comment_db:
        yield {
            "user_db": mock_user_db,
            "post_db": mock_post_db,
            "comment_db": mock_comment_db
        }


@pytest.fixture
def mock_http():
    with patch("httpx.get") as mock_get:
        yield mock_get


def test_load_data(mock_db, mock_http):
    mock_response = MagicMock()
    mock_response.json.return_value = [{"id": 1, "name": "John Doe"}]
    mock_http.return_value = mock_response

    response = client.get("/load_data")
    assert response.status_code == 200
    assert response.json() == {"message": "Data loaded successfully"}
    assert mock_http.call_count == 3
    assert mock_db["user_db"].insert_one.call_count == 1
    assert mock_db["post_db"].insert_one.call_count == 1
    assert mock_db["comment_db"].insert_one.call_count == 1


def test_get_post_count(mock_db):
    mock_db["user_db"].find_one.return_value = {"id": 1, "name": "John Doe"}
    mock_db["post_db"].count_documents.return_value = 5

    response = client.get("/get_post_count/1")
    assert response.status_code == 200
    data = response.json()
    assert data == {"user": {"id": 1, "name": "John Doe"}, "post_count": 5}


def test_get_comments(mock_db):
    mock_db["post_db"].find_one.return_value = {"id": 1, "title": "Post Title"}
    mock_db["comment_db"].find.return_value = [{"id": 1, "body": "Comment body"}]

    response = client.get("/get_comments/1")
    assert response.status_code == 200
    data = response.json()
    assert "Post Title" in str(data)


def test_get_users(mock_db):
    mock_db["user_db"].find.return_value = [{"id": 1, "name": "John Doe"}]

    response = client.get("/get_users")
    assert response.status_code == 200
    data = response.json()
    assert data == {"users": [{"id": 1, "name": "John Doe"}]}


def test_get_user(mock_db):
    mock_db["user_db"].find_one.return_value = {"id": 1, "name": "John Doe"}

    response = client.get("/get_user/1")
    assert response.status_code == 200
    data = response.json()
    assert data == {"user": {"id": 1, "name": "John Doe"}}


def test_add_user(mock_db):
    response = client.post("/create_user", json=mock_user_data)
    assert response.status_code == 200
    assert response.json() == {"message": "User created successfully"}
    mock_db["user_db"].insert_one.assert_called_once()


def test_update_user(mock_db):
    mock_db["user_db"].update_one.return_value.acknowledged = True
    response = client.put("/update_user/1", json=mock_user_data)
    assert response.status_code == 200
    assert response.json() == {"message": "User updated successfully"}


def test_delete_user(mock_db):
    mock_db["user_db"].delete_one.return_value.acknowledged = True

    response = client.delete("/delete_user/1")
    assert response.status_code == 200
    assert response.json() == {"message": "User deleted successfully"}
    mock_db["user_db"].delete_one.assert_called_once()
