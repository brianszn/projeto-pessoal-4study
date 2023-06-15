
from fastapi import FastAPI, APIRouter, HTTPException, status, Response
from models.models import User, users

router = APIRouter()


@router.get('/users', summary='Obter todos os usuarios')

async def getUsers():
    return users

@router.post('/users', summary='Cadastrar um usuario', response_model=User)

async def cadUsers(user: User):
    users.append(user)
    return user


@router.get('/users/{id}', summary='Obter um usuario por ID', response_model=User)

async def getUserById(id: int):
    for user in users:
        if user.id == id:
            return user
        else:
            exist = False
    if not exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')

@router.delete('/users/{id}', summary='Deletar um usuario por ID', response_model=User)

async def deleteUserById(id: int):
    for user in users:
        if user.id == id:
            users.remove(user)
            return {'msg':f'Usuario {user.username} removido'}
        else:
            exist = False
    if not exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found', response_model=User)


@router.put('/users/{id}', summary='Atualizar um usuario por ID', response_model=User)

async def putUserById(user: User, id: int):
    for userExist in users:
        if userExist.id == id:
            userExist.username = user.username
            return user
        else:
            exist = False
    if not exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')