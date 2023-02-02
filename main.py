from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

@app.get("/blog")
def index(limit=10, published:bool = True, sort: Optional[str]=None):
    
    #only get 10 published blogs
    #/blog?limit=10&published=true
    
    if published:
        return {"data":f" {limit} published blogs List from the db"}
    else:
        return {'data':f"{limit} blogs from the db"}


@app.get('/unpublished')
def unpublished():
    return {'data':'all unpublished data'}


@app.get('/{id}')
def show(id:int):
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id, limit = 10):

    return {'data':{'1','2'}}



class Blog(BaseModel):
    title :str
    body: str
    published:Optional[bool]
    

@app.post('/blog')
def create_blog(blog:Blog):
    
    return {"data":f"blog is created {blog.title}"}


