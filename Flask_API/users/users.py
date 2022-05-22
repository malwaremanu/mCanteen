import os
from fastapi import FastAPI, Request
from fastapi import APIRouter
router = APIRouter()

from deta import Deta
from dotenv import load_dotenv
load_dotenv()
deta = Deta(os.getenv('deta_key'))

users = deta.Base("users")

# Get working
@router.get('/users/')
async def getUsers():
    respose={}
    # fetches all the users from Deta cloud db
    allusers=users.fetch()
    for item in allusers.items:
        respose[item["key"]]=item["user"]
    return respose


@router.delete('/users/{id}')
async def deleteUsers(id:str):
    users.delete(id)
    return {
        "status" : "SUCCESS",
        "message":f"user with id {id} deleted"
    }

@router.put('/users/{id}')
async def updateUsers(id:str, request : Request):
    try:
        r = await request.json()
        print(r.get('empno'))    
        users.put({"user":r},id)
        #return {"message":f"user with id {id} updated"}
        return {
            "status" : "SUCCESS",
            "message":f"user with id {id} updated",
            "data" : r
        }
    except:
        return {
            "status" : "ERROR",
            "message":f"user with id {id} was not updated",
        }

# Post working 
@router.post('/users/')
async def postUsers(request : Request):
    # id:str and user: str implies input validation, ie the url parameters can be of only type string
    r = await request.json()
    users.insert({"user":r})
    return {
        "status" : "SUCCESS",
        "message" : "User created successfully",
        "data" : r
    }
