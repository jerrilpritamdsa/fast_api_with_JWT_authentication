from pydantic import BaseModel
from typing import List, Union




class BlogBase(BaseModel):
    title:str
    body:str
    
class Blog(BlogBase):
    class Config():
        orm_mode = True

class UserBase(BaseModel):
    name:str
    email:str
    password:str

class User(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode = True
    
    


# similarly to the below response model we must provoide the
# user details with only user name and email and not show password 
 
class ShowUser(BaseModel):
    name:str
    email:str
    blogs : List[Blog]
    class Config():
        orm_mode = True

# this class provides a response model that only provides with
# title and body and no ID
class ShowBlog(BaseModel):
    title:str
    body:str
    creator: User
    class Config():
        orm_mode = True
        
        
class Login(BaseModel):
    username:str
    password:str
    
    
# these are from the fast api JWT documentation

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None