from fastapi import FastAPI, HTTPException, status, Response
from models.models import User, users
from routes import user_router, root_router

app = FastAPI(title='My little API docs', version='0.0.1', description='Practicing best practices in API development')

app.include_router(user_router.router, tags=['Users Routers'])
app.include_router(root_router.router, tags=['Root Routers'])

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True, log_level='info')