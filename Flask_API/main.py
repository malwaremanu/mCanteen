import os
from fastapi import FastAPI, Request
from deta import Deta

from dotenv import load_dotenv
load_dotenv()

#deta = Deta("c0qm30mo_ZAEx1mTufH9EyGpDivRP3p56x1PxoqzY")
deta = Deta(os.getenv('deta_key'))

app = FastAPI()

users = deta.Base("users")

# Get working
@app.get('/users/')
async def getUsers():
    respose={}
    # fetches all the users from Deta cloud db
    allusers=users.fetch()
    for item in allusers.items:
        respose[item["key"]]=item["user"]
    return respose

# # Adds a user with two parameters, id of the user and the content of the user
# @app.get('/users/add/{id}/{user}')
# async def adduser(id:str,user:str):
#     # id:str and user: str implies input validation, ie the url parameters can be of only type string
#     users.insert({"user":user},id)
#     # inserts a user with key as id
#     print(f"user inserted with id: {id}")
#     return {"message":"user added!"}

# Post working 
@app.post('/users/')
async def postUsers(request : Request):
    # id:str and user: str implies input validation, ie the url parameters can be of only type string
    r = await request.json()
    users.insert({"user":r})
    return {
        "status" : "SUCCESS",
        "message" : "User created successfully",
        "data" : r
    }

# Delete working
@app.delete('/users/{id}')
async def deleteUsers(id:str):
    users.delete(id)
    return {
        "status" : "SUCCESS",
        "message":f"user with id {id} deleted"
    }

# Update working
@app.put('/users/{id}')
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