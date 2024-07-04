import httpx
from pymongo import errors

from dbconn import user_db, post_db, comment_db
from model import User, UpdateUser


def load_data(urls):
    for key, url in urls.items():
        try:
            response = httpx.get(url)
            response.raise_for_status()
            data = response.json()
            for item in data:
                try:
                    if key == 'users':
                        user_db.insert_one(item)
                    elif key == 'posts':
                        post_db.insert_one(item)
                    elif key == 'comments':
                        comment_db.insert_one(item)
                except errors.PyMongoError as e:
                    print(f"Error inserting {key} data into MongoDB: {e}")
                    exit()
        except httpx.RequestError as e:
            print(f"Error fetching data from {url}: {e}")
            exit()
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred while fetching data from {url}: {e}")
            exit()
    return {'message': 'Data loaded successfully'}


def get_post_count(user_id):
    try:
        _filter = {'id': int(user_id)}
        projection = {'_id': 0}
        user = user_db.find_one(_filter, projection)
        post_count = post_db.count_documents({'userId': int(user_id)})
        return {'user': user, 'post_count': post_count}
    except errors.PyMongoError as e:
        return {'message': f'Could not fetch data from database: {e}'}
    except Exception as e:
        return {'message': f'An unexpected error occurred: {e}'}


def get_comments(post_id):
    try:
        _filter = {'id': int(post_id)}
        projection = {'_id': 0}
        post = post_db.find_one(_filter, projection)
        filter2 = {'postId': int(post_id)}
        comments = comment_db.find(filter2, projection)
        return {'post': post, 'comments': list(comments)}
    except errors.PyMongoError as e:
        return {'message': f'Could not fetch data from database: {e}'}
    except Exception as e:
        return {'message': f'An unexpected error occurred: {e}'}


def get_users():
    try:
        _filter = {'_id': 0}
        users = user_db.find(projection=_filter)
        return {'users': list(users)}
    except errors.PyMongoError as e:
        return {'message': f'Could not fetch data from database: {e}'}
    except Exception as e:
        return {'message': f'An unexpected error occurred: {e}'}


def get_user(user_id):
    try:
        _filter = {'id': user_id}
        projection = {'_id': 0}
        user = user_db.find_one(_filter, projection)
        if user is not None:
            return {'user': user}
        else:
            return {'message': 'User not found'}
    except errors.PyMongoError as e:
        return {'message': f'Could not fetch data from database: {e}'}
    except Exception as e:
        return {'message': f'An unexpected error occurred: {e}'}


def add_user(user: UpdateUser):
    try:
        new_id = user_db.count_documents({}) + 1
        user = User(id=new_id, **user.dict())
        user_db.insert_one(user.dict())
        return {'message': 'User created successfully'}
    except errors.PyMongoError as e:
        return {'message': f'Could not create the user: {e}'}
    except Exception as e:
        return {'message': f'An unexpected error occurred: {e}'}


def update_user(user_id, user: UpdateUser):
    try:
        query = {'id': user_id}
        _filter = {'$set': user.dict()}
        ack = user_db.update_one(query, _filter)
        if ack.acknowledged:
            return {'message': 'User updated successfully'}
        else:
            return {'message': 'Could not update the user'}
    except errors.PyMongoError as e:
        return {'message': f'Could not update the user: {e}'}
    except Exception as e:
        return {'message': f'An unexpected error occurred: {e}'}


def delete_user(user_id):
    try:
        query = {'id': user_id}
        ack = user_db.delete_one(query)
        if ack.acknowledged:
            return {'message': 'User deleted successfully'}
        else:
            return {'message': 'Could not delete the user'}
    except errors.PyMongoError as e:
        return {'message': f'Could not delete the user: {e}'}
    except Exception as e:
        return {'message': f'An unexpected error occurred: {e}'}
