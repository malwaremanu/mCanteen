import os
from fastapi import FastAPI, Request
from fastapi import APIRouter
router = APIRouter()

from deta import Deta
from dotenv import load_dotenv
load_dotenv()
deta = Deta(os.getenv('deta_key'))

products = deta.Base("products")

# Delete working
@router.delete('/products/{id}')
async def deleteProducts(id:str):
    products.delete(id)
    return {
        "status" : "SUCCESS",
        "message":f"product with id {id} deleted"
    }

# Update working
@router.put('/products/{id}')
async def updateProducts(id:str, request : Request):
    try:
        r = await request.json()
        print(r.get('empno'))    
        products.put({"product":r},id)        
        return {
            "status" : "SUCCESS",
            "message":f"product with id {id} updated",
            "data" : r
        }
    except:
        return {
            "status" : "ERROR",
            "message":f"product with id {id} was not updated",
        }


@router.post('/products/')
async def postProducts(request : Request):
    # id:str and product: str implies input validation, ie the url parameters can be of only type string
    r = await request.json()
    products.insert({"product":r})
    return {
        "status" : "SUCCESS",
        "message" : "product created successfully",
        "data" : r
    }


@router.get('/products/')
async def getProducts():
    respose={}
    # fetches all the products from Deta cloud db
    allproducts=products.fetch()
    for item in allproducts.items:
        respose[item["key"]]=item["product"]
    return respose
    