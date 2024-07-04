from fastapi import APIRouter

from crud import load_data, get_post_count, get_comments, get_users, get_user, update_user, delete_user, add_user
from model import UpdateUser

router = APIRouter()


@router.get('/load_data', tags=["Data Load"], summary="Load data from a External API to MongoDB")
def load_to_data():
    urls = {
        'users': 'https://jsonplaceholder.typicode.com/users',
        'posts': 'https://jsonplaceholder.typicode.com/posts',
        'comments': 'https://jsonplaceholder.typicode.com/comments'
    }
    return load_data(urls)


@router.get('/get_post_count/{user_id}', tags=["Posts & Comments"],
            summary="Get the count of posts & comments based on user or post from the  database")
def get_post_count_user(user_id: int):
    data = get_post_count(user_id)
    return data


@router.get('/get_comments/{post_id}', tags=["Posts & Comments"],
            summary="Get the comments based on post_id from the database")
def get_comments_post(post_id: int):
    data = get_comments(post_id)
    return data


@router.get('/get_users', tags=["Users"], summary="Get all users from the database")
def all_users():
    users = get_users()
    return users


@router.get('/get_user/{user_id}', tags=["Users"], summary="Get a user based on user_id from the database")
def get_single_user(user_id: int):
    user = get_user(user_id)
    return user


@router.post('/create_user', tags=["Users"], summary="Create a user in the database")
def new_user(user: UpdateUser):
    return add_user(user)


@router.put('/update_user/{user_id}', tags=["Users"], summary="Update a user in the database")
def update_user_data(user_id: int, user: UpdateUser):
    return update_user(user_id, user)


@router.delete('/delete_user/{user_id}', tags=["Users"], summary="Delete a user from the database")
def delete_user_data(user_id: int):
    return delete_user(user_id)
