from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, models, token



router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

get_db = database.get_db

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def all(db: Session= Depends(get_db), current_user:schemas.User = Depends(token.get_current_user)):
    blogs = db.query(models.Blog).all()
    return blogs




@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog, db: Session = Depends(get_db), current_user:schemas.User = Depends(token.get_current_user)):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = 2)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db), current_user:schemas.User = Depends(token.get_current_user)):
    blog = db.query(models.Blog).filter((models.Blog.id == id)).delete(synchronize_session=False)
    db.commit()
    return 'the blog post deleted'

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id,response:Response, db: Session= Depends(get_db), current_user:schemas.User = Depends(token.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the ID {id} not available')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f'Blog with the ID {id} not available'}
    return blog


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request:schemas.Blog, db: Session= Depends(get_db), current_user:schemas.User = Depends(token.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog woth id {id} not found")
    blog.update(request.dict())
    db.commit()
    return 'Updated'
    

