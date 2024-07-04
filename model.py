from pydantic import BaseModel


# Solution 1 that developing the model based on the data from the API
class Geo(BaseModel):
    lat: str
    lng: str


class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo


class Company(BaseModel):
    name: str
    catchPhrase: str
    bs: str


class User(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company


class UpdateUser(BaseModel):
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company

# Solution 2 that generates the model based on the data from the API


# api_url = 'https://jsonplaceholder.typicode.com/users/1'
# response = httpx.get(api_url)
# data = response.json()


# def generate_model_from_dict(name: str, data_dict: Dict[str, Any]) -> BaseModel:
#     fields = {}
#     for key, value in data_dict.items():
#         if isinstance(value, dict):
#             nested_model = generate_model_from_dict(key, value)
#             fields[key] = (nested_model, ...)
#         elif isinstance(value, list):
#             if value and isinstance(value[0], dict):
#                 nested_model = generate_model_from_dict(key, value[0])
#                 fields[key] = (List[nested_model], ...)
#             else:
#                 fields[key] = (type(value[0]) if value else Any, ...)
#         else:
#             fields[key] = (type(value), ...)
#     return create_model(name, **fields)


# User = generate_model_from_dict('User', data)
# UpdateUser = generate_model_from_dict('UpdateUser', data, exclude={'id'})
