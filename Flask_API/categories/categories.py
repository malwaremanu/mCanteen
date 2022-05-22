import os, datetime
from fastapi import FastAPI, Request
from fastapi import APIRouter
router = APIRouter()

from deta import Deta
from dotenv import load_dotenv
load_dotenv()
deta = Deta(os.getenv('deta_key'))

categories = deta.Base("categories")

# Delete working
@router.delete('/categories/{id}')
async def deletecategories(id:str):
    categories.delete(id)
    return {
        "status" : "SUCCESS",
        "message":f"category with id {id} deleted"
    }

# Update working
@router.put('/categories/{id}')
async def updatecategories(id:str, request : Request):
    try:
        r = await request.json()    
        r['created_on'] = str(datetime.datetime.now())    
        categories.put({"category":r},id)        
        return {
            "status" : "SUCCESS",
            "message":f"category with id {id} updated",
            "data" : r
        }
    except:
        return {
            "status" : "ERROR",
            "message":f"category with id {id} was not updated",
        }


@router.post('/categories/')
async def postcategories(request : Request):
    # id:str and category: str implies input validation, ie the url parameters can be of only type string
    r = await request.json()
    r['created_on'] = str(datetime.datetime.now())    
    categories.insert({"category":r})
    return {
        "status" : "SUCCESS",
        "message" : "category created successfully",
        "data" : r
    }


@router.get('/categories/')
async def getcategories():
    respose={}
    # fetches all the categorys from Deta cloud db
    allcategories=categories.fetch()
    for item in allcategories.items:
        print(item)
        respose[item["key"]]=item["category"]
    return respose
    