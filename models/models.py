from typing import Optional, List, Dict, List
from pydantic import BaseModel, validator
import re



class User(BaseModel):

    id: int
    username: str
    email: str

    @validator('email')

    def check_email(cls, value):
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", value):
            raise ValueError('Invalid email address')
        return value
 
    @validator('username')
    def check_username(cls, value):
        if not re.match(r'^[a-zA-Z0-9_]+$', value):
            raise ValueError('Invalid username')
        return value


     
users = [
    User(id=1, username='test', email='pvtbrian@mail.com'),
    User(id=2, username='Leon', email='Leon@mail.com'),
    User(id=3, username='Ashley', email='Ashley@mail.com')
]

